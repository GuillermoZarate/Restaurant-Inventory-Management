from django.shortcuts import render

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def inventory(request):
    return render(request, 'inventory/main_page_inventory.html')
