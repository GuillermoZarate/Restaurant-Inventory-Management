
from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def home(request):
    context = {'name': request.user}
    return render(request, 'main/home.html', context)

def logout_request(request):
    logout(request)
    return redirect("home")

@login_required
def inventory(request):
    return render(request, 'main/inventory.html')

@login_required
def menu(request):
    return render(request, 'main/menu.html')

@login_required
def purchases(request):
    return render(request, 'main/purchases.html')