from django.contrib import admin
from cardapio.models import Produto, Pizza, Ingrediente, Bebida, PizzaIngrediente

# Register your models here.

admin.site.register(Produto)
admin.site.register(Pizza)
admin.site.register(Ingrediente)
admin.site.register(Bebida)
admin.site.register(PizzaIngrediente)


