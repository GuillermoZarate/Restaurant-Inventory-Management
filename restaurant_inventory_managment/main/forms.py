from django import forms
from .models import Ingredient, MenuItem

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'price_unit']

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'