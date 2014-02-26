from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.template import RequestContext, loader

from clientes.models import Cliente, Endereco

def index(request):
  template = loader.get_template('clientes/index.html')
  return HttpResponse(template.render(RequestContext(request)))

def consulta(request):
  if request.method == 'POST':
    try:
      cliente = Cliente.objects.get(email=request.POST['email'])
    except (Cliente.DoesNotExist):
      raise Http404
    else:
      return redirect('/clientes/%d' % cliente.id)
  else:
    raise PermissionDenied

def dados(request, cliente_id):
  try:
    cliente = Cliente.objects.get(pk=cliente_id)
  except (Cliente.DoesNotExist):
    raise Http404
  else:
    return render(request, 'clientes/enderecos.html', {
      'cliente': cliente
      }
    )

def enderecoNovo(request, cliente_id):
  try:
    cliente = Cliente.objects.get(pk=cliente_id)
  except (Cliente.DoesNotExist):
    raise Http404
  else:
    return render(request, 'clientes/endereco.html', {
      'cliente': cliente
      }
    )

def enderecoDeletar(request, cliente_id, endereco_id):
  try:
    cliente = Cliente.objects.get(pk=cliente_id)
    endereco = Endereco.objects.get(pk=endereco_id)
  except (Cliente.DoesNotExist):
    raise Http404
  else:
    endereco.delete()
    return redirect('/clientes/%d' % cliente.id)

def enderecoAdicionar(request, cliente_id):
  if request.method == 'POST':
    try:
      cliente = Cliente.objects.get(pk=cliente_id)
      endereco = cliente.endereco_set.create(cep=request.POST['cep'], logradouro=request.POST['logradouro'], numero=request.POST['numero'], bairro=request.POST['bairro'], cidade=request.POST['cidade'], estado=request.POST['estado'])
    except (Cliente.DoesNotExist):
      raise Http404
    else:
      return redirect('/clientes/%d' % cliente.id)
  else:
    raise PermissionDenied
