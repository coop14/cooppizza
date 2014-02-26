from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from produto.models import Produto

def index(request):
    latest_produto_list = Produto.objects.order_by('-id')[:5]
    context = {'latest_produto_list': latest_produto_list}
    return render(request, 'produto/index.html', context)
	
def detail(request, produto_id):
	return HttpResponse("You're looking at poll %s." % produto_id)

def results(request, produto_id):
    return HttpResponse("You're looking at the results of poll %s." % produto_id)

def vote(request, produto_id):
    return HttpResponse("You're voting on poll %s." % produto_id)
