from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.template import RequestContext, loader
from django.core.exceptions import PermissionDenied
from cooppizza.cardapio.models import PromocoesDaPizzaria, Produto, Ingrediente, Item

def promoIndex(request):
	return render(request, 'promocao/index.html')

def promoCriar(request):
	latest_produto_list = Produto.objects.all().order_by('-id')
	latest_ingrediente_list = Ingrediente.objects.all().order_by('-id')
	context = {'latest_produto_list': latest_produto_list, 'latest_ingrediente_list' : latest_ingrediente_list}
	return render(request, 'promocao/criar.html', context)

def promoAdicionar(request):
	if request.method == 'POST':
		try:
			promocao = PromocoesDaPizzaria.objects.get(nome=request.POST['nome'])
			raise PermissionDenied
		except (PromocoesDaPizzaria.DoesNotExist):
			nome=request.POST['nome']
			dataInicio=request.POST['dataInicio']
			dataTermino=request.POST['dataTermino']
			desconto=request.POST['desconto']
			itemExtra=request.POST['itemExtra']
			produtoBase = request.POST['produtoBase']
			quantiaProdutoBase = request.POST['quantiaProdutoBase']
			ingredienteBase = request.POST['ingredienteBase']
			diaBase = request.POST['diaBase']
			choice = request.POST['base']
			if int(choice) == 1:
				ingredienteBase = 0
				diaBase = 0
			elif int(choice) == 2:
				produtoBase = 0
				quantiaProdutoBase = 0
				diaBase = 0
			elif int(choice) == 3:
				produtoBase = 0
				quantiaProdutoBase = 0
				ingredienteBase = 0
				promocao = PromocoesDaPizzaria(nome=nome, dataInicio=dataInicio, dataTermino=dataTermino, desconto=desconto, itemExtra=itemExtra, produtoBase=produtoBase, quantiaProdutoBase=quantiaProdutoBase, ingredienteBase=ingredienteBase, diaBase=diaBase)
			promocao.save()
			return redirect('/promocao/%d' % promocao.id)
	else:
		raise PermissionDenied
		return render(request, 'promocao/index.html')
		
def promoListar(request):
	latest_promo_list = PromocoesDaPizzaria.objects.all().order_by('-id')
	context = {'latest_promo_list': latest_promo_list}
	return render(request, 'promocao/listar.html', context)
	
def promoEditar(request, promocao_id):
	if request.method == 'POST':
		try:
			promocao = PromocoesDaPizzaria.objects.get(pk=promocao_id)
			promocao.nome = request.POST['nome']
			promocao.dataInicio = request.POST['dataInicio']
			promocao.dataTermino = request.POST['dataTermino']
			promocao.desconto = request.POST['desconto']
			promocao.itemExtra = request.POST['itemExtra']
			produtoBase = request.POST['produtoBase']
			quantiaProdutoBase = request.POST['quantiaProdutoBase']
			ingredienteBase = request.POST['ingredienteBase']
			diaBase = request.POST['diaBase']
			choice = request.POST['base']
			if int(choice) == 1:
				promocao.produtoBase = produtoBase
				promocao.quantiaProdutoBase = quantiaProdutoBase
				promocao.ingredienteBase = 0
				promocao.diaBase = 0
			elif int(choice) == 2:
				promocao.produtoBase = 0
				promocao.quantiaProdutoBase = 0
				promocao.ingredienteBase = ingredienteBase
				promocao.diaBase = 0
			elif int(choice) == 3:
				promocao.produtoBase = 0
				promocao.quantiaProdutoBase = 0
				promocao.ingredienteBase = 0
				promocao.diaBase = diaBase
			promocao.save()
		except (PromocoesDaPizzaria.DoesNotExist):
			raise Http404
		return redirect('/promocao/%d' % promocao.id)
	else:
		raise PermissionDenied

def promoExcluir(request, promocao_id):
	try:
		promocao = PromocoesDaPizzaria.objects.get(pk=promocao_id)
		promocao.delete()
	except (PromocoesDaPizzaria.DoesNotExist):
		raise Http404
	latest_promo_list = PromocoesDaPizzaria.objects.all().order_by('-id')
	context = {'latest_promo_list': latest_promo_list}
	return render(request, 'promocao/listar.html', context)

def promoConsultar(request, promocao_id):
	try:
		promocao = PromocoesDaPizzaria.objects.get(pk=promocao_id)
		latest_produto_list = Produto.objects.all().order_by('-id')
		latest_ingrediente_list = Ingrediente.objects.all().order_by('-id')
		
		stringDataInicio = str(promocao.dataInicio.year)
		if promocao.dataInicio.month >= 10:
			stringDataInicio += '-'+str(promocao.dataInicio.month)
		else:
			stringDataInicio += '-0'+str(promocao.dataInicio.month)
		if promocao.dataInicio.day >= 10:
			stringDataInicio += '-'+str(promocao.dataInicio.day)
		else:
			stringDataInicio += '-0'+str(promocao.dataInicio.day)
		
		stringDataTermino = str(promocao.dataTermino.year)
		if promocao.dataTermino.month >= 10:
			stringDataTermino += '-'+str(promocao.dataTermino.month)
		else:
			stringDataTermino += '-0'+str(promocao.dataTermino.month)
		if promocao.dataTermino.day >= 10:
			stringDataTermino += '-'+str(promocao.dataTermino.day)
		else:
			stringDataTermino += '-0'+str(promocao.dataTermino.day)
		
		if int(promocao.produtoBase) == 0 and int(promocao.ingredienteBase) == 0:
			checkProduto=3
		elif int(promocao.produtoBase) == 0 and int(promocao.diaBase) == 0:
			checkProduto=2
		elif int(promocao.produtoBase) == 0 and int(promocao.ingredienteBase) == 0:
			checkProduto=1
		context = {'latest_produto_list': latest_produto_list, 'latest_ingrediente_list' : latest_ingrediente_list, 'promocao': promocao, 'checkProduto': checkProduto, 'stringDataInicio': stringDataInicio, 'stringDataTermino': stringDataTermino}
	except PromocoesDaPizzaria.DoesNotExist:
		raise Http404
	return render(request, 'promocao/promocao.html', context )
