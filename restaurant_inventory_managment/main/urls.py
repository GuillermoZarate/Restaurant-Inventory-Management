from django.urls import path, include
from .views import IngredientListView   

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout', views.logout_request, name='logout'),
    path('inventory/', IngredientListView.as_view(), name="inventory"),
    path('menu/', views.menu, name="menu"),
    path('purchases/', views.purchases, name="purchases")
]