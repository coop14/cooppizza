from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied

from cooppizza.cardapio.models import Produto, Pizza, Ingrediente, Bebida, PizzaIngrediente, Item

def indexPedido(request):
  template = loader.get_template('indexPedido.html')
  return HttpResponse(template.render(RequestContext(request)))

def pizzasPedido(request):
	try:
		pizzas = Pizza.objects.all()
		ingredientes = Ingrediente.objects.all()
		pizzasingredientes = PizzaIngrediente.objects.all()
	except (Pizza.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'pizzasPedido.html', {'pizzas':pizzas,
		'ingredientes':ingredientes, 'pizzasingredientes':pizzasingredientes})

def bebidasPedido(request):
	try:
		bebidas = Bebida.objects.all()
	except (Bebida.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'bebidasPedido.html', {'bebidas':bebidas})

def bebidaAdiciona(request, bebida_id):
	if request.method == "POST":
		bebida = Bebida.objects.get(pk=bebida_id)
		produto = bebida.produto
		item = Item(produto = produto,
			quantidade = request.POST['quantidade'],
    		preco = produto.preco,
    		promocao = False,
    		observacao = request.POST['observacao'])
		item.save()
		return redirect(reverse('ingrediente'))
	else:
		raise PermissionDenied

def carrinhoPedido(request, produto_id):
	try:
		produto_id = Produto.objects.get(pk=produto_id)
	except (Produto.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'carrinhoPedido.html',
		 {'produto':produto})
