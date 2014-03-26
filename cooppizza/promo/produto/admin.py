from django.contrib import admin

from produto.models import Produto
class ProdutoAdmin(admin.ModelAdmin):
    fields = ['name', 'preco', 'desconto']

admin.site.register(Produto, ProdutoAdmin)
