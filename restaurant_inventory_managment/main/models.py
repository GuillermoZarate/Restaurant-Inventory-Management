from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Ingredient(models.Model):
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z ]+$',
        message='El nombre solo puede contener letras y espacios.',
        code='invalid_name'
    )

    name = models.CharField(max_length=100, unique=True, validators=[name_validator])
    quantity = models.PositiveIntegerField()
    price_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.quantity} units" 

class MenuItem(models.Model):
    menu_item = models.CharField(max_length=100, unique=True)
    price_entry = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='', null=True, blank=True)  # Agregamos un campo de imagen

    def __str__(self):
        return self.menu_item

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    quantity_required = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.menu_item} - {self.ingredient} ({self.quantity_required} units)"
    
class Purchase(models.Model):
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    quantity_purchased = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.menu_item} - {self.quantity_purchased} units purchased on {self.purchase_date}"