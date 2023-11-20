
from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from .models import Ingredient
from .tables import IngredientTable
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
    paginate_by = 3  

    def get_queryset(self):
        # Order the queryset by name
        return Ingredient.objects.all().order_by('name')