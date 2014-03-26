from django.db import models
from decimal import Decimal

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
    isRecheio = models.BooleanField()
    
class PromocoesDaPizzaria(models.Model):
	def __unicode__(self): 
		return self.nome
	nome = models.CharField(max_length=100)
	itemExtra = models.ForeignKey(Produto)
	dataInicio = models.DateField()
	dataTermino = models.DateField()
	desconto = models.DecimalField(max_digits=7 , decimal_places=2)
