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
  pizzas = Pizza.objects.all()
  ingredientes = Ingrediente.objects.all()
  pizzasingredientes = PizzaIngrediente.objects.all()
  return render(request, 'pizzasPedido.html', {'pizzas':pizzas, 'ingredientes':ingredientes, 'pizzasingredientes':pizzasingredientes})

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

def carrinhoPedido(request):
  itens = []
  total = 0
  for k in request.session.iterkeys():
    if k.startswith('pid_'):
      if request.session[k] > 0:
        total += request.session[k]
        produto = Produto.objects.get(pk=k[4:])
        itens.append({'produto': produto, 'quantidade': request.session[k]})
  return render(request, 'carrinhoPedido.html', {'itens': itens, 'total': total})

def carrinhoPedidoAdicionar(request, produto_id):
  try:
    produto = Produto.objects.get(pk=produto_id)
  except (Produto.DoesNotExist):
    raise Http404
  else:
    if request.session.get('pid_%d' % produto.id, 0):
      request.session['pid_%d' % produto.id] += 1
    else:
      request.session['pid_%d' % produto.id] = 1
    
    return redirect(pizzasPedido)

def carrinhoPedidoRemover(request, produto_id):
  if request.session.get('pid_' + produto_id, 0):
    request.session['pid_' + produto_id] = 0
  return redirect(carrinhoPedido)
