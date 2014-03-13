from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.template import RequestContext, loader
from django.core.exceptions import PermissionDenied
from produto.models import Produto

def index(request):
	template = loader.get_template('produto/index.html')
	return HttpResponse(template.render(RequestContext(request)))

def promoListar(request):
	latest_produto_list = Produto.objects.all().order_by('-id')
	context = {'latest_produto_list': latest_produto_list}
	return render(request, 'produto/listar.html', context)
	
def promoEditar(request, produto_id):
	if request.method == 'POST':
		try:
			produto = Produto.objects.get(pk=produto_id)
			produto.desconto = request.POST['desconto']
			produto.promocao = True
			produto.save()
		except (Produto.DoesNotExist):
			raise Http404
		return redirect('/produto/%d' % produto.id)
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
	return redirect('/produto/%d' % produto.id)

def promoConsultar(request, produto_id):
	try:
		produto = Produto.objects.get(pk=produto_id)
	except Produto.DoesNotExist:
		raise Http404
	return render(request, 'produto/promocao.html', {'produto': produto})
