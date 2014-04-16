from django.db import models
import datetime
from django.utils import timezone
from cooppizza.clientes.models import Cliente, Endereco

# Create your models here.

class Produto(models.Model):
    def __unicode__(self): 
        return self.nome
    nome = models.CharField(max_length=200, unique=True)
    preco = models.DecimalField(max_digits=7 , decimal_places=2)
    isPizza = models.BooleanField()

class Ingrediente(models.Model):
    def __unicode__(self):
        return self.nome
    nome = models.CharField(max_length=200, unique=True)
    marca = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300, default="-")

class Pizza(models.Model):
    def __unicode__(self):
        return self.produto.nome
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
        return self.produto.nome
    produto = models.ForeignKey(Produto)

class PizzaIngrediente(models.Model):
    def __unicode__(self): 
        return u'%s %s' % (self.pizza.produto.nome, self.ingrediente.nome)
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
    isRecheio = models.BooleanField(default=True)



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
        return u'%s %s' % (self.quantidade, self.produto.nome)
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
    observacao = models.CharField(max_length=400)
    
class PromocoesDaPizzaria(models.Model):
	def __unicode__(self): 
		return self.nome
	nome = models.CharField(max_length=100)
	produtoBase = models.IntegerField()
	quantiaProdutoBase = models.IntegerField()
	ingredienteBase = models.IntegerField()
	DIAS_SEMANA = (
		('Domingo', 1),
		('Segunda', 2),
		('Terca', 3),
		('Quarta', 4),
		('Quinta', 5),
		('Sexta', 6),
		('Sabado', 7),
	)
	diaBase = models.IntegerField(choices=DIAS_SEMANA)
	itemExtra = models.IntegerField()
	dataInicio = models.DateField()
	dataTermino = models.DateField()
	desconto = models.DecimalField(max_digits=7 , decimal_places=2)

class Pagamento(models.Model):
    def __unicode__(self): 
        return self.valorTotal
    pedido = models.ForeignKey(Pedido) 
    metodoPagamento = models.CharField(max_length=100)
    valorTotal = models.DecimalField(max_digits=7 , decimal_places=2)
    precisaTroco = models.BooleanField()
    promocao = models.ForeignKey(PromocoesDaPizzaria)
    status = models.BooleanField()
