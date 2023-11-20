import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from .models import Ingredient
class IngredientTable(tables.Table):
    edit = tables.Column(empty_values=(), orderable=False)
    delete = tables.Column(empty_values=(), orderable=False)
    class Meta:
        model = Ingredient
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'class': 'table table-bordered table-hover ', 'data-searching': 'true',}

    def render_edit(self, record):
        return format_html('<button>Editar</button>')

    def render_delete(self, record):
        return format_html('<button>Eliminar</button>')

