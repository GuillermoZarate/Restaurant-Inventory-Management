
from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from .models import Ingredient
from .tables import IngredientTable
from .forms import IngredientForm 
from django_tables2 import SingleTableView

@login_required
def home(request):
    context = {'name': request.user}
    return render(request, 'main/home.html', context)

def logout_request(request):
    logout(request)
    return redirect("home")

@login_required
def menu(request):
    return render(request, 'main/menu.html')

@login_required
def purchases(request):
    return render(request, 'main/purchases.html')

@method_decorator(login_required, name='dispatch')
class IngredientListView(LoginRequiredMixin, SingleTableView):
    model = Ingredient
    table_class = IngredientTable
    template_name = 'main/inventory.html'
    paginate_by = 10

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
            return self.get(request, *args, **kwargs)  # Redirige a la vista de lista (get request)
        else:
            # Si el formulario no es válido, vuelva a renderizar la página con el formulario y la tabla
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)
    