from django.contrib import admin
from tabelas.models import Pizzaria
from tabelas.models import Funcionarios
from tabelas.models import Contrato
# Register your models here.

admin.site.register(Pizzaria)
admin.site.register(Funcionarios)
admin.site.register(Contrato)
