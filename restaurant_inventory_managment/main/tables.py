import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from .models import Ingredient, Purchase

class IngredientTable(tables.Table):
    edit = tables.Column(empty_values=(), orderable=False)
    delete = tables.Column(empty_values=(), orderable=False)
    class Meta:
        model = Ingredient
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'class': 'table table-bordered table-hover ', 'data-searching': 'true',}
        exclude = ('id',)

    def render_delete(self, record):
        return format_html('<a class="delete-button" href="{}"><i class="fa-solid fa-trash"></i><span>Delete</span></a>', reverse('delete_ingredient', args=[record.id]))


    def render_edit(self, record):
        return format_html('<a class="edit-button" href="{}"><i class="fa-solid fa-pen-to-square"></i><span>Edit</span></a>', reverse('update_ingredient', args=[record.id]))

class PurchaseTable(tables.Table):
    class Meta:
        model = Purchase
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'class': 'table table-bordered table-hover ', 'data-searching': 'true',}
        exclude = ('id',)