from django.db import models

# Create your models here.

class Pedido(models.Model):
  cliente = models.ForeignKey(clientes.models.Cliente)
  telefone = models.CharField(max_length=15)
  cep = models.CharField(max_length=8)
  logradouro = models.CharField(max_length=50)
  numero = models.CharField(max_length=5)
  complemento = models.CharField(max_length=50)
  bairro = models.CharField(max_length=50)
  cidade = models.CharField(max_length=50)
  estado = models.CharField(max_length=2)
  status = models.
  def __unicode__(self):
    return self.cep

class PedidoItens(models.Model):
  pedido = models.ForeignKey(Pedido)
