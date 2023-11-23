from django import forms
from .models import Ingredient, MenuItem, Purchase

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'price_unit']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'