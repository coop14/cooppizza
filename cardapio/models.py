from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class pagamento
    pedido
    metodoPagamento
    valorTotal
    precisaTroco
    promocao
    status(foi pago?)

class pedido
    status
    cliente
    endereco
    telefone
    isdelivery

class promocoesDaPizzaria
    item
    itemExtra

class item
    pedido
    produto
    quantidade
    agrupamento
    preco
    promocao

class pizza2sabores


class Produto(models.Model):
    def __unicode__(self): 
		return self.name
    name = models.CharField(max_length=200, unique=True)
    preco = models.DecimalField(max_digits=7 , decimal_places=2)
    # promocao = models.BooleanField()
    # desconto = models.DecimalField(max_digits=7, decimal_places=2)
    ispizza

class Ingrediente(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=200, unique=True)
    quantidadeEstoque = models.DecimalField(max_digits=7, decimal_places=3)

class Pizza(models.Model):
    def __unicode__(self):
		return self.produto.name
    produto = models.ForeignKey(Produto)
    tamanho
    tipoDePizza = models.CharField(max_length=200)
    ingredientes = models.ManyToManyField(Ingrediente, through='PizzaIngrediente')

class Bebida(models.Model):
    def __unicode__(self):
		return self.produto.name
    produto = models.ForeignKey(Produto)

class PizzaIngrediente(models.Model):
	quantidadeDeUso = models.DecimalField(max_digits=7, decimal_places=3)
	pizza = models.ForeignKey(Pizza)
	ingrediente = models.ForeignKey(Ingrediente)

