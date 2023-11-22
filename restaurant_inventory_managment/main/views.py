
from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from .models import Ingredient, MenuItem
from .tables import IngredientTable
from .forms import IngredientForm, MenuForm 
from django_tables2 import SingleTableView, LazyPaginator
from django.contrib import messages # Manejo de errores y envio de mensajes

from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView


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