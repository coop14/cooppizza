from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied

from cooppizza.cardapio.models import Produto, Pizza, Ingrediente, Bebida, PizzaIngrediente

# Create your views here.

def indexCardapio(request):
	template = loader.get_template('indexCardapio.html')
	return HttpResponse(template.render(RequestContext(request)))

def pizza(request):
	try:
		pizzas = Pizza.objects.all()
	except (Pizza.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'pizza.html', {'pizzas':pizzas})	

def bebida(request):
	try:
		bebidas = Bebida.objects.all()
	except (Bebida.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'bebida.html', {'bebidas':bebidas})	

def ingrediente(request):
	try:
		ingredientes = Ingrediente.objects.all()
	except (Ingrediente.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'ingrediente.html', {'ingredientes':ingredientes})	

def ingredienteNovo(request):
	return render(request, 'ingredienteNovo.html')

def ingredienteCadastrar(request):
	if request.method == "POST":
		ingrediente = Ingrediente(nome=request.POST['nome'], marca=request.POST['marca'], descricao=request.POST['descricao'])
		ingrediente.save()
		return redirect(reverse('ingredienteDados', args=[ingrediente.id]))
	else:
		raise PermissionDenied

def ingredienteConsulta(request, ingrediente_id):
	try:
		ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
	except (Ingrediente.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'ingredienteDados.html',
		 {'ingrediente':ingrediente})

def ingredienteAltera(request, ingrediente_id):
	try:
		ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
	except (Ingrediente.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'ingredienteAltera.html',
		 {'ingrediente':ingrediente})

def ingredienteEdita(request, ingrediente_id):
	if request.method == "POST":
		try:
			ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
			ingrediente.quantidadeEstoque = request.POST['quantidadeEstoque']
			ingrediente.save()
		except (Ingrediente.DoesNotExist):
			raise Http404
		else: 
			return redirect(reverse('ingredienteDados', args=[ingrediente.id]))
  	else:
  		raise PermissionDenied


def ingredienteDados(request, ingrediente_id):
	try:
		ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
	except (Ingrediente.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'ingredienteDados.html',
		 {'ingrediente':ingrediente})

def ingredienteDeletar(request, ingrediente_id):
  try:
    ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
  except (Ingrediente.DoesNotExist):
    raise Http404
  else:
    ingrediente.delete()
    return redirect(reverse('ingrediente'))

def pizzaNova(request):
	return render(request, 'pizzaNova.html')

def pizzaCadastrar(request):
	if request.method == "POST":
		produto = Produto(nome=request.POST['nome'], preco=request.POST['preco'], isPizza=True)
		produto.save()
		pizza = Pizza(produto=produto, tipoDePizza = request.POST['tipoDePizza'], tamanho=request.POST['tamanho'])
		pizza.save()
		return redirect(reverse('pizzaDados', args=[pizza.id]))
	else:
		raise PermissionDenied

def pizzaConsulta(request, pizza_id):
	try:
		pizza = Pizza.objects.get(pk=pizza_id)
	except (Pizza.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'pizzaDados.html',
		 {'pizza':pizza})

def pizzaAltera(request, pizza_id):
	try:
		pizza = Pizza.objects.get(pk=pizza_id)
	except (Pizza.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'pizzaAltera.html',
		 {'pizza':pizza})

def pizzaEdita(request, pizza_id):
	if request.method == "POST":
		try:
			pizza = Pizza.objects.get(pk=pizza_id)
			produto = pizza.produto
			produto.preco = request.POST['preco']
			produto.save()
		except (Pizza.DoesNotExist):
			raise Http404
		else: 
			return redirect(reverse('pizzaDados', args=[pizza.id]))
  	else:
  		raise PermissionDenied

def pizzaDados(request, pizza_id):
	try:
		pizza = Pizza.objects.get(pk=pizza_id)
	except (Pizza.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'pizzaDados.html',
		 {'pizza':pizza})

def pizzaDeletar(request, pizza_id):
  try:
    pizza = Pizza.objects.get(pk=pizza_id)
    produto = pizza.produto
  except (Pizza.DoesNotExist):
    raise Http404
  else:
    pizza.delete()
    produto.delete()
    return redirect(reverse('pizza'))

def pizzaDeletarIngrediente(request, pizza_id, pizzaingrediente_id):
  try:
    pizza = Pizza.objects.get(pk=pizza_id)
    pizzaIngrediente = PizzaIngrediente.objects.get(pk=pizzaingrediente_id)
  except (Pizza.DoesNotExist):
    raise Http404
  else:
    pizzaIngrediente.delete()
    return redirect(reverse('pizzaDados', args=[pizza.id]))

def pizzaIngrediente(request, pizza_id):
	try:
		pizza = Pizza.objects.get(pk=pizza_id)
		ingredientes = Ingrediente.objects.all().order_by('nome')
	except (Pizza.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'pizzaIngrediente.html',
		 {'pizza':pizza, 'ingredientes':ingredientes})

def pizzaIngredienteAdiciona(request, pizza_id):
	if request.method == "POST":
		try:
			ingrediente = Ingrediente.objects.get(nome=request.POST['nome'])
			pizza = Pizza.objects.get(pk=pizza_id)
			if request.POST.__contains__('isRecheio'):
				pizzaIngrediente = PizzaIngrediente(quantidadeDeUso=request.POST['quantidadeDeUso'], pizza=pizza, ingrediente=ingrediente, medida=request.POST['medida'], isRecheio=True) 
			else:
				pizzaIngrediente = PizzaIngrediente(quantidadeDeUso=request.POST['quantidadeDeUso'], pizza=pizza, ingrediente=ingrediente, medida=request.POST['medida'], isRecheio=False) 
			pizzaIngrediente.save()
		except (Ingrediente.DoesNotExist):
			raise Http404
		else: 
			return redirect(reverse('pizzaDados', args=[pizza.id]))
  	else:
  		raise PermissionDenied

def bebidaNova(request):
	return render(request, 'bebidaNova.html')

def bebidaCadastrar(request):
	if request.method == "POST":
		produto = Produto(nome=request.POST['nome'], preco=request.POST['preco'], isPizza=False)
		produto.save()
		bebida = Bebida(produto=produto)
		bebida.save()
		return redirect(reverse('bebidaDados', args=[bebida.id]))
	else:
		raise PermissionDenied

def bebidaConsulta(request, bebida_id):
	try:
		bebida = Bebida.objects.get(pk=bebida_id)
	except (Bebida.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'bebidaDados.html',
		 {'bebida':bebida})

def bebidaAltera(request, bebida_id):
	try:
		bebida = Bebida.objects.get(pk=bebida_id)
	except (Bebida.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'bebidaAltera.html',
		 {'bebida':bebida})

def bebidaEdita(request, bebida_id):
	if request.method == "POST":
		try:
			bebida = Bebida.objects.get(pk=bebida_id)
			produto = bebida.produto
			produto.preco = request.POST['preco']
			produto.save()
		except (Bebida.DoesNotExist):
			raise Http404
		else: 
			return redirect(reverse('bebidaDados', args=[bebida.id]))
  	else:
  		raise PermissionDenied

def bebidaDados(request, bebida_id):
	try:
		bebida = Bebida.objects.get(pk=bebida_id)
	except (Bebida.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'bebidaDados.html',
		 {'bebida':bebida})

def bebidaDeletar(request, bebida_id):
  try:
    bebida = Bebida.objects.get(pk=bebida_id)
    produto = bebida.produto
  except (Bebida.DoesNotExist):
    raise Http404
  else:
    bebida.delete()
    produto.delete()
    return redirect(reverse('bebida'))

def listaProduto(request):
	produtos = Produto.objects.all().order_by('-preco')
	return render(request, 'listaProduto.html', {'produtos':produtos})



