
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from .models import Ingredient, MenuItem, RecipeRequirement
from .tables import IngredientTable
from .forms import IngredientForm, MenuForm 
from django_tables2 import SingleTableView, LazyPaginator
from django.contrib import messages # Manejo de errores y envio de mensajes

from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView

from .cart import Cart
from django.http import JsonResponse

def logout_request(request):
    logout(request)
    return redirect("home")

@login_required
def purchases(request):
    return render(request, 'main/purchases.html')

@method_decorator(login_required, name='dispatch')
class MenuListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'main/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Agrega el formulario al contexto si es necesario
        context['menu'] = MenuItem.objects.all().order_by('menu_item')
        return context
    
@method_decorator(login_required, name='dispatch')
class IngredientListView(LoginRequiredMixin, SingleTableView):
    model = Ingredient
    table_class = IngredientTable
    template_name = 'main/inventory.html'
    paginate_by = 10
    pagination_class = LazyPaginator

    def get_queryset(self):
        return Ingredient.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IngredientForm()  # Agrega el formulario al contexto
        return context

    def post(self, request, *args, **kwargs):
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ingrediente guardado exitosamente.')
        else:
            messages.error(request, 'Hubo un error al guardar el ingrediente. Por favor, corrige los errores.')
        
        return self.get(request, *args, **kwargs)  # Redirige a la vista de lista (get request)

@method_decorator(login_required, name='dispatch')
class DeleteInventoryItemView(DeleteView):
    model = Ingredient
    success_url = '/inventory'  # Redirect to "/lines" after successful deletion
    template_name = 'main/delete_ingredient.html'
@method_decorator(login_required, name='dispatch')
class UpdateInventoryItemView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = '/inventory' 
    template_name = 'main/update_ingredient.html'


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(MenuItem, id=product_id)

        cart.add(product=product)
        cart_quantity = cart.__len__()

        response_data = {
            'qty': cart_quantity,
            'product_id': product_id  # Agregar el product_id a la respuesta
        }

        return JsonResponse(response_data)


# Create context processor so our cart can work on all pages of the site
def cart(request):
	# Return the default data from our Cart
	return {'cart': Cart(request)}

def confirm_selection(request):
    cart = Cart(request)

    # Obtener la información de los elementos seleccionados
    selected_items = cart.cart
    
    final_dict = {}

    # Itera sobre los ítems seleccionados
    for menu_item_id, details in selected_items.items():
        # Obtén el objeto MenuItem
        menu_item = MenuItem.objects.get(pk=int(menu_item_id))

        # Obtén los requisitos de receta asociados a ese ítem de menú
        recipe_requirements = RecipeRequirement.objects.filter(menu_item=menu_item)

        # Crea un diccionario para almacenar la información del ítem seleccionado
        item_info = {
            'menu_item_name': menu_item.menu_item,
            'menu_item_price': details['price'],
            'ingredients': []
        }

        # Itera sobre los requisitos de receta y obtén la información del ingrediente
        for requirement in recipe_requirements:
            ingredient = requirement.ingredient
            quantity_required = requirement.quantity_required

            # Calcula el precio total del ingrediente (precio unitario * cantidad requerida)
            ingredient_price = ingredient.price_unit * quantity_required

            # Agrega la información del ingrediente al diccionario
            item_info['ingredients'].append({
                'ingredient_name': ingredient.name,
                'ingredient_quantity': quantity_required,
                'ingredient_price': ingredient_price
            })

        # Agrega la información del ítem seleccionado al diccionario final
        final_dict[menu_item_id] = item_info

    # Limpiar el carrito después de confirmar la selección
    cart.cart = {}
    cart.session['cart'] = {}
    cart.session.modified = True

    return render(request, 'main/confirm_selection.html', {'selected_items': final_dict})