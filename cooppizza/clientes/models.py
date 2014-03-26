from django.db import models

class Cliente(models.Model):
  telefone = models.CharField(max_length=15)
  email = models.CharField(max_length=50)
  senha = models.CharField(max_length=20)
  def __unicode__(self):
    return self.email

class Endereco(models.Model):
  cliente = models.ForeignKey(Cliente)
  cep = models.CharField(max_length=8)
  logradouro = models.CharField(max_length=50)
  numero = models.CharField(max_length=5)
  complemento = models.CharField(max_length=50)
  bairro = models.CharField(max_length=50)
  cidade = models.CharField(max_length=50)
  estado = models.CharField(max_length=2)
  def __unicode__(self):
    return self.cep
