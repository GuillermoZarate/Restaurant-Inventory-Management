from django.urls import path, include
from .views import IngredientListView, DeleteInventoryItemView, UpdateInventoryItemView, MenuListView 

from . import views

urlpatterns = [
    path('', MenuListView.as_view(), name="menu"),
    path('add/', views.cart_add, name='cart_add'),
    path('logout', views.logout_request, name='logout'),
    path('inventory/', IngredientListView.as_view(), name="inventory"),
    path('inventory/delete/<pk>', DeleteInventoryItemView.as_view(), name='delete_ingredient'),
    path('inventory/update/<pk>', UpdateInventoryItemView.as_view(), name='update_ingredient'),
    path('purchases/', views.purchases, name="purchases"),
]