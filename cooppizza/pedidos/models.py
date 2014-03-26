from django.db import models
import datetime
from django.utils import timezone
from clientes.models import Cliente, Endereco


class Produto(models.Model):
    def __unicode__(self): 
        return self.name
    name = models.CharField(max_length=200, unique=True)
    preco = models.DecimalField(max_digits=7 , decimal_places=2)
    isPizza = models.BooleanField()

class Ingrediente(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=200, unique=True)
    quantidadeEstoque = models.DecimalField(max_digits=7, decimal_places=3)
    isRecheio = models.BooleanField()

class Pizza(models.Model):
    def __unicode__(self):
        return self.produto.name
    produto = models.ForeignKey(Produto)
    GRANDE = 'G'
    MEDIA = 'M'
    PEQUENA = 'P'
    TAMANHO_CHOICES = (
        (GRANDE, 'Grande'),
        (MEDIA, 'Media'),
        (PEQUENA, 'Pequena'),
    )
    tamanho = models.CharField(max_length=1, choices=TAMANHO_CHOICES)
    tipoDePizza = models.CharField(max_length=200)
    ingredientes = models.ManyToManyField(Ingrediente, through='PizzaIngrediente')

class Bebida(models.Model):
    def __unicode__(self):
        return self.produto.name
    produto = models.ForeignKey(Produto)

class PizzaIngrediente(models.Model):
    pizza = models.ForeignKey(Pizza)
    ingrediente = models.ForeignKey(Ingrediente)
    quantidadeDeUso = models.DecimalField(max_digits=7, decimal_places=3)
    KILOGRAMA = 'KG'
    PITADA = 'PT'
    XICARA = 'XC'
    COLHER = 'CL'
    MEDIDA_CHOICES = (
        (KILOGRAMA, 'Kilograma'),
        (PITADA, 'Pitada'),
        (XICARA, 'Xicara'),
        (COLHER, 'Colher'),
    )
    medida = models.CharField(max_length=2, choices=MEDIDA_CHOICES)

class Pedido(models.Model):
    def __unicode__(self): 
        return self.cliente.nome
    status = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente) 
    endereco = models.ForeignKey(Endereco) 
    telefone = models.CharField(max_length=100)
    isdelivery = models.BooleanField()
    data = models.DateField(auto_now_add=True)

class Item(models.Model):
    def __unicode__(self):
        return self.produto.name
    produto = models.ForeignKey(Produto)
    pedido = models.ForeignKey(Pedido)
    quantidade = models.DecimalField(max_digits=7 , decimal_places=2)
    UM = 'UM'
    DOIS = 'DO'
    TRES = 'TR'
    AGRUPAMENTO_CHOICES = (
        (UM, 'Um'),
        (DOIS, 'Dois'),
        (TRES, 'Tres'),
    )
    agrupamento = models.CharField(max_length=2, choices=AGRUPAMENTO_CHOICES)
    preco = models.DecimalField(max_digits=7 , decimal_places=2)
    promocao = models.BooleanField()
    observacao = telefone = models.CharField(max_length=400)

class PromocoesDaPizzaria(models.Model):
    def __unicode__(self): 
        return self.nome
    nome = models.CharField(max_length=100)
    item = models.ForeignKey(Item)
    itemExtra = models.ForeignKey(Produto)
    dataInicio = models.DateField()
    dataTermino = models.DateField()

class Pagamento(models.Model):
    def __unicode__(self): 
        return self.valorTotal
    pedido = models.ForeignKey(Pedido) 
    metodoPagamento = models.CharField(max_length=100)
    valorTotal = models.DecimalField(max_digits=7 , decimal_places=2)
    precisaTroco = models.BooleanField()
    promocao = models.ForeignKey(PromocoesDaPizzaria)
    status = models.BooleanField()

