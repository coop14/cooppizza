from django.db import models

# Create your models here.

class Pizzaria(models.Model):
	nome_piz = models.CharField(max_length=45)
	telefone = models.CharField(max_length=45)
	cnpj = models.CharField(max_length=45)
	def __unicode__(self):
		return self.nome_piz
		return self.telefone
		return self.cnpj


class Funcionarios(models.Model):
	pizzaria = models.ForeignKey(Pizzaria)
	nome_func = models.CharField(max_length=1024)
	idade = models.IntegerField()
	sexo = models.CharField(max_length=1)
	cargo = models.CharField(max_length=45)
	def __unicode__(self):
		return self.nome_func
		return self.idade
		return self.sexo
		return self.cargo


class Contrato(models.Model):
	funcionario = models.ForeignKey(Funcionarios)
	valorpago = models.CharField(max_length=45)
	periodo = models.CharField(max_length=45)
	cargahoraria = models.CharField(max_length=45)
	def __unicode__(self):
		return self.valorpago
		return self.periodo
		return cargahoraria

class Produtos(models.Model):
	produto = models.CharField(max_length=45)
	def __unicode__(self):
		return self.produto

class Estoques(models.Model):
	produto = models.ForeignKey(Produtos)
	quantidade = models.CharField(max_length=45)
	valorminimo = models.CharField(max_length=45)
	def __unicode__(self):
		return self.estoque


