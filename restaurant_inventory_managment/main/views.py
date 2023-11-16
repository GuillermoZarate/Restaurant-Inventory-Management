
from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def home(request):
    return render(request, 'main/home.html')

@login_required
def inventory(request):
    return render(request, 'main/inventory.html')

def logout_request(request):
    logout(request)
    return redirect("home")