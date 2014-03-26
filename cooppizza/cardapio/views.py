from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied

from cardapio.models import Produto, Pizza, Ingrediente, Bebida, PizzaIngrediente

# Create your views here.

def base(request):
	template = loader.get_template('cardapio/base.html')
	return HttpResponse(template.render(RequestContext(request)))

def index(request):
	template = loader.get_template('cardapio/index.html')
	return HttpResponse(template.render(RequestContext(request)))

def pizza(request):
	return render(request, 'cardapio/pizza.html')

def bebida(request):
	return render(request, 'cardapio/bebida.html')

def ingrediente(request):
	return render(request, 'cardapio/ingrediente.html')

def ingredienteNovo(request):
	return render(request, 'cardapio/ingredienteNovo.html')

def ingredienteCadastrar(request):
	if request.method == "POST":
		ingrediente = Ingrediente(name=request.POST['name'], quantidadeEstoque=request.POST['quantidadeEstoque'])
		ingrediente.save()
		return redirect('/cardapio/ingrediente/%d' % ingrediente.id)
	else:
		raise PermissionDenied

def ingredienteConsulta(request):
	if request.method == 'POST':
	    try:
	      ingrediente = Ingrediente.objects.get(name=request.POST['name'])
	    except (Ingrediente.DoesNotExist):
	      raise Http404
	    else:
	      return redirect('/cardapio/ingrediente/%d' % ingrediente.id)
  	else:
  		raise PermissionDenied

def ingredienteAltera(request, ingrediente_id):
	try:
		ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
	except (Ingrediente.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'cardapio/ingredienteAltera.html',
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
			return redirect('/cardapio/ingrediente/%d' % ingrediente.id)
  	else:
  		raise PermissionDenied


def ingredienteDados(request, ingrediente_id):
	try:
		ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
	except (Ingrediente.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'cardapio/ingredienteDados.html',
		 {'ingrediente':ingrediente})

def ingredienteDeletar(request, ingrediente_id):
  try:
    ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
  except (Ingrediente.DoesNotExist):
    raise Http404
  else:
    ingrediente.delete()
    return redirect('/cardapio/ingrediente/')

def pizzaNova(request):
	return render(request, 'cardapio/pizzaNova.html')

def pizzaCadastrar(request):
	if request.method == "POST":
		produto = Produto(name=request.POST['name'], preco=request.POST['preco'], desconto=0, promocao=0)
		produto.save()
		pizza = Pizza(produto=produto, tipoDePizza = request.POST['tipoDePizza'])
		pizza.save()
		return redirect('/cardapio/pizza/%d' % pizza.id)
	else:
		raise PermissionDenied

def pizzaConsulta(request):
	if request.method == 'POST':
	    try:
	      produto = Produto.objects.get(name=request.POST['name'])
	      pizza = Pizza.objects.get(produto=produto)
	    except (Pizza.DoesNotExist):
	      raise Http404
	    else:
	      return redirect('/cardapio/pizza/%d' % pizza.id)
  	else:
  		raise PermissionDenied

def pizzaAltera(request, pizza_id):
	try:
		pizza = Pizza.objects.get(pk=pizza_id)
	except (Pizza.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'cardapio/pizzaAltera.html',
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
			return redirect('/cardapio/pizza/%d' % pizza.id)
  	else:
  		raise PermissionDenied

def pizzaDados(request, pizza_id):
	try:
		pizza = Pizza.objects.get(pk=pizza_id)
	except (Pizza.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'cardapio/pizzaDados.html',
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
    return redirect('/cardapio/pizza/')

def pizzaDeletarIngrediente(request, pizza_id, pizzaingrediente_id):
  try:
    pizza = Pizza.objects.get(pk=pizza_id)
    pizzaIngrediente = PizzaIngrediente.objects.get(pk=pizzaingrediente_id)
  except (Pizza.DoesNotExist):
    raise Http404
  else:
    pizzaIngrediente.delete()
    return redirect('/cardapio/pizza/%d' % pizza.id)

def pizzaIngrediente(request, pizza_id):
	try:
		pizza = Pizza.objects.get(pk=pizza_id)
		ingredientes = Ingrediente.objects.all().order_by('name')
	except (Pizza.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'cardapio/pizzaIngrediente.html',
		 {'pizza':pizza, 'ingredientes':ingredientes})

def pizzaIngredienteAdiciona(request, pizza_id):
	if request.method == "POST":
		try:
			ingrediente = Ingrediente.objects.get(name=request.POST['name'])
			pizza = Pizza.objects.get(pk=pizza_id)
			pizzaIngrediente = PizzaIngrediente(quantidadeDeUso=request.POST['quantidadeDeUso'], pizza=pizza, ingrediente=ingrediente) 
			pizzaIngrediente.save()
		except (Ingrediente.DoesNotExist):
			raise Http404
		else: 
			return redirect('/cardapio/pizza/%d' % pizza.id)
  	else:
  		raise PermissionDenied

def bebidaNova(request):
	return render(request, 'cardapio/bebidaNova.html')

def bebidaCadastrar(request):
	if request.method == "POST":
		produto = Produto(name=request.POST['name'], preco=request.POST['preco'], desconto=0, promocao=0)
		produto.save()
		bebida = Bebida(produto=produto)
		bebida.save()
		return redirect('/cardapio/bebida/%d' % bebida.id)
	else:
		raise PermissionDenied

def bebidaConsulta(request):
	if request.method == 'POST':
	    try:
	      produto = Produto.objects.get(name=request.POST['name'])
	      bebida = Bebida.objects.get(produto=produto)
	    except (Bebida.DoesNotExist):
	      raise Http404
	    else:
	      return redirect('/cardapio/bebida/%d' % bebida.id)
  	else:
  		raise PermissionDenied

def bebidaAltera(request, bebida_id):
	try:
		bebida = Bebida.objects.get(pk=bebida_id)
	except (Bebida.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'cardapio/bebidaAltera.html',
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
			return redirect('/cardapio/bebida/%d' % bebida.id)
  	else:
  		raise PermissionDenied

def bebidaDados(request, bebida_id):
	try:
		bebida = Bebida.objects.get(pk=bebida_id)
	except (Bebida.DoesNotExist):
		raise Http404
	else: 
		return render(request, 'cardapio/bebidaDados.html',
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
    return redirect('/cardapio/bebida/')

def listaProduto(request):
	produtos = Produto.objects.all().order_by('-preco')
	return render(request, 'cardapio/listaProduto.html', {'produtos':produtos})


