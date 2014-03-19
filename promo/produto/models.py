from django.db import models
from decimal import Decimal

class Produto(models.Model):
	name = models.CharField(max_length=200)
	preco = models.DecimalField(default=Decimal('0.00'), max_digits=7, decimal_places=2)
	promocao = models.BooleanField(default=False)
	desconto = models.DecimalField(default=Decimal('0.00'), max_digits=7, decimal_places=2)
	def __unicode__(self):
		return self.name