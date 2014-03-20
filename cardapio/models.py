from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class pagamento(models.Model):

    pedido = models.ForeignKey(Pedido) 
    metodoPagamento = models.CharField(max_length=100)
    valorTotal = models.DecimalField(max_digits=7 , decimal_places=2)
    precisaTroco = models.BooleanField(required=False)
    promocao = models.ForeignKey(PromocoesDaPizzaria)
    status = models.BooleanField(required=True)

class Pedido(models.Model):
    def __unicode__(self): 
        return self.cliente.nome
    status = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente) 
    endereco = models.ForeignKey(Endereco) 
    telefone = models.CharField(max_length=100)
    isdelivery = models.BooleanField(required=True)

class PromocoesDaPizzaria(models.Model):
    def __unicode__(self): 
        return self.nome
    nome = models.CharField(max_length=100)
    item = models.ForeignKey(Item)
    itemExtra = models.ForeignKey(Item)

class Item(models.Model):
    pedido = models.ForeignKey(Pedido)
    produto = models.ForeignKey(Produto)
    quantidade = models.DecimalField(max_digits=7 , decimal_places=2)
    agrupamento = models.DecimalField(max_digits=1)
    preco = models.DecimalField(max_digits=7 , decimal_places=2)
    promocao = models.BooleanField(required=True)
    observacao = telefone = models.CharField(max_length=400)

class Produto(models.Model):
    def __unicode__(self): 
		return self.name
    name = models.CharField(max_length=200, unique=True)
    preco = models.DecimalField(max_digits=7 , decimal_places=2)
    ispizza = models.BooleanField(required=True)

class Ingrediente(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=200, unique=True)
    quantidadeEstoque = models.DecimalField(max_digits=7, decimal_places=3)
    isrecheio

class Pizza(models.Model):
    def __unicode__(self):
		return self.produto.name
    produto = models.ForeignKey(Produto)
    tamanho = models.CharField(max_length=1)
    tipoDePizza = models.CharField(max_length=200)
    ingredientes = models.ManyToManyField(Ingrediente, through='PizzaIngrediente')

class Bebida(models.Model):
    def __unicode__(self):
		return self.produto.name
    produto = models.ForeignKey(Produto)

class PizzaIngrediente(models.Model):
	quantidadeDeUso = models.DecimalField(max_digits=7, decimal_places=3)
    medida = models.CharField(max_lenght=100)
	pizza = models.ForeignKey(Pizza)
	ingrediente = models.ForeignKey(Ingrediente)

