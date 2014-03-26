from django.contrib import admin
from tabelas.models import Pizzaria, Funcionarios, Contrato, Produtos, Estoques

# Register your models here.

class ContratoInline(admin.TabularInline):
    model = Contrato
    extra = 0

class FuncionarioAdmin(admin.ModelAdmin):
   
    fieldsets = [
        (None,               {'fields': ['nome_func']}),
        ('Details Information', {'fields': ['idade', 'sexo', 'cargo'], 'classes': ['collapse']}),
    ]
    inlines = [ContratoInline]
    list_display = ('nome_func', 'idade', 'sexo', 'cargo')

class FuncionariosInline(admin.TabularInline):
    model = Funcionarios
    extra = 0

class PizzariaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nome_piz']}),
        ('Details Information', {'fields': ['telefone', 'cnpj'], 'classes': ['collapse']}),
    ]
    inlines = [FuncionariosInline]

class EstoquesInline(admin.TabularInline):
    model = Estoques
    extra = 0

class ProdutosAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['produto']}),
    ]
    inlines = [EstoquesInline]


admin.site.register(Pizzaria, PizzariaAdmin)

admin.site.register(Funcionarios, FuncionarioAdmin)
admin.site.register(Produtos, ProdutosAdmin)

