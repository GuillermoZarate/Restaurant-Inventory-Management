from django.urls import path, include
from .views import IngredientListView, DeleteInventoryItemView, UpdateInventoryItemView 

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout', views.logout_request, name='logout'),
    path('inventory/', IngredientListView.as_view(), name="inventory"),
    path('inventory/delete/<pk>', DeleteInventoryItemView.as_view(), name='delete_ingredient'),
    path('inventory/update/<pk>', UpdateInventoryItemView.as_view(), name='update_ingredient'),
    path('menu/', views.menu, name="menu"),
    path('purchases/', views.purchases, name="purchases"),
]