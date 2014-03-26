from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied

from cooppizza.cardapio.models import Produto, Pizza, Ingrediente, Bebida, PizzaIngrediente

# Create your views here.

def index(request):
	template = loader.get_template('indexCardapio.html')
	return HttpResponse(template.render(RequestContext(request)))

def pizza(request):
	return render(request, 'pizza.html')

def bebida(request):
	return render(request, 'bebida.html')

def ingrediente(request):
	return render(request, 'ingrediente.html')

def ingredienteNovo(request):
	return render(request, 'ingredienteNovo.html')

def ingredienteCadastrar(request):
	if request.method == "POST":
		ingrediente = Ingrediente(nome=request.POST['nome'], quantidadeEstoque=request.POST['quantidadeEstoque'], isRecheio=True)
		ingrediente.save()
		return redirect(reverse('ingredienteDados', args=[ingrediente.id]))
	else:
		raise PermissionDenied

def ingredienteConsulta(request):
	if request.method == 'POST':
	    try:
	      ingrediente = Ingrediente.objects.get(nome=request.POST['nome'])
	    except (Ingrediente.DoesNotExist):
	      raise Http404
	    else:
	      return redirect(reverse('ingredienteDados', args=[ingrediente.id]))
  	else:
  		raise PermissionDenied

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
		pizza = Pizza(produto=produto, tipoDePizza = request.POST['tipoDePizza'])
		pizza.save()
		return redirect(reverse('pizzaDados', args=[pizza.id]))
	else:
		raise PermissionDenied

def pizzaConsulta(request):
	if request.method == 'POST':
	    try:
	      produto = Produto.objects.get(nome=request.POST['nome'])
	      pizza = Pizza.objects.get(produto=produto)
	    except (Pizza.DoesNotExist):
	      raise Http404
	    else:
	      return redirect(reverse('pizzaDados', args=[pizza.id]))
  	else:
  		raise PermissionDenied

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
			pizzaIngrediente = PizzaIngrediente(quantidadeDeUso=request.POST['quantidadeDeUso'], pizza=pizza, ingrediente=ingrediente) 
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
		produto = Produto(nome=request.POST['nome'], preco=request.POST['preco'], desconto=0, promocao=0)
		produto.save()
		bebida = Bebida(produto=produto)
		bebida.save()
		return redirect(reverse('bebidaDados', args=[bebida.id]))
	else:
		raise PermissionDenied

def bebidaConsulta(request):
	if request.method == 'POST':
	    try:
	      produto = Produto.objects.get(nome=request.POST['nome'])
	      bebida = Bebida.objects.get(produto=produto)
	    except (Bebida.DoesNotExist):
	      raise Http404
	    else:
	      return redirect(reverse('bebidaDados', args=[bebida.id]))
  	else:
  		raise PermissionDenied

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


