from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.template import RequestContext, loader
from django.core.exceptions import PermissionDenied
from produto.models import PromocoesDaPizzaria, Produto, Ingrediente

def index(request):
	return render(request, 'promocao/index.html')

def promoCriar(request):
	latest_produto_list = Produto.objects.all().order_by('-id')
	latest_ingrediente_list = Ingrediente.objects.all().order_by('-id')
	context = {'latest_produto_list': latest_produto_list, 'latest_ingrediente_list' : latest_ingrediente_list}
	return render(request, 'promocao/criar.html', context)

def promoAdicionar(request):
	if request.method == 'POST':
		try:
			produto = Produto.objects.get(pk=produto_id)
			produto.desconto = request.POST['desconto']
			produto.promocao = True
			produto.save()
		except (Produto.DoesNotExist):
			raise Http404
		return redirect('/promocao/%d' % produto.id)
	else:
		raise PermissionDenied
		
def promoListar(request):
	latest_promo_list = PromocoesDaPizzaria.objects.all().order_by('-id')
	context = {'latest_promo_list': latest_promo_list}
	return render(request, 'promocao/listar.html', context)
	
def promoEditar(request, produto_id):
	if request.method == 'POST':
		try:
			produto = Produto.objects.get(pk=produto_id)
			produto.desconto = request.POST['desconto']
			produto.promocao = True
			produto.save()
		except (Produto.DoesNotExist):
			raise Http404
		return redirect('/promocao/%d' % produto.id)
	else:
		raise PermissionDenied

def promoExcluir(request, produto_id):
	try:
		produto = Produto.objects.get(pk=produto_id)
		produto.desconto = '0.00'
		produto.promocao = False
		produto.save()
	except (Produto.DoesNotExist):
		raise Http404
	return redirect('/promocao/%d' % produto.id)

def promoConsultar(request, produto_id):
	try:
		produto = Produto.objects.get(pk=produto_id)
	except Produto.DoesNotExist:
		raise Http404
	return render(request, 'promocao/promocao.html', {'produto': produto})
