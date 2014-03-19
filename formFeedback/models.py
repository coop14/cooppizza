from django.db import models
from django import forms
import datetime

# Create your models here.

class FeedbackForm(forms.Form):
	assunto = forms.CharField(max_length=100)
	escolhaDoAssunto = forms.CharField(max_length=100)
	detalheDoAssunto = forms.CharField(max_length=100)
	dataDoFeedback =  forms.DateTimeField(initial=datetime.date.today)
	tipoDePedido = forms.CharField(max_length=100)
	formaDePedido = forms.CharField(max_length=100)
	precoPedido = forms.DecimalField(max_digits=7 , decimal_places=2)
	observacoes = forms.CharField(max_length=1000)
	nota = forms.DecimalField(max_digits=1)
	respostaDoFeedback = forms.BooleanField(required=False)
