from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.template import RequestContext, loader

from clientes.models import Cliente, Endereco

def web(request):
  template = loader.get_template('clientes/indexWeb.html')
  return HttpResponse(template.render(RequestContext(request)))

def webAcesso(request):
  if request.method == 'POST':
    try:
      cliente = Cliente.objects.get(email=request.POST['email'])
    except (Cliente.DoesNotExist):
      raise Http404
    else:
      if cliente.senha == request.POST['senha']:
        return redirect('/pedidos/')
      else:
        raise PermissionDenied
  else:
    raise PermissionDenied

def index(request):
  template = loader.get_template('clientes/index.html')
  return HttpResponse(template.render(RequestContext(request)))

def clienteNovo(request):
  return render(request, 'clientes/cliente.html')

def clienteAdicionar(request):
  if request.method == 'POST':
    try:
      cliente = Cliente.objects.get(email=request.POST['email'])
      raise PermissionDenied
    except (Cliente.DoesNotExist):
      cliente = Cliente(email=request.POST['email'], telefone=request.POST['telefone'], senha="123")
      cliente.save()
      return redirect('/clientes/%d' % cliente.id)
  else:
    raise PermissionDenied

def clienteConsulta(request):
  if request.method == 'POST':
    try:
      cliente = Cliente.objects.get(telefone=request.POST['telefone'])
    except (Cliente.DoesNotExist):
      try:
        cliente = Cliente.objects.get(email=request.POST['email'])
      except (Cliente.DoesNotExist):
        raise Http404
      else:
        return redirect('/clientes/%d' % cliente.id)
    else:
      return redirect('/clientes/%d' % cliente.id)
  else:
    raise PermissionDenied

def clienteDados(request, cliente_id):
  try:
    cliente = Cliente.objects.get(pk=cliente_id)
  except (Cliente.DoesNotExist):
    raise Http404
  else:
    return render(request, 'clientes/enderecos.html', {
      'cliente': cliente
      }
    )

def clienteLista(request):
  clientes = Cliente.objects.all()
  return render(request, 'clientes/clientes.html', {
    'clientes': clientes
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
      endereco = cliente.endereco_set.create(cep=request.POST['cep'], logradouro=request.POST['logradouro'], numero=request.POST['numero'], complemento=request.POST['complemento'], bairro=request.POST['bairro'], cidade=request.POST['cidade'], estado=request.POST['estado'])
    except (Cliente.DoesNotExist):
      raise Http404
    else:
      return redirect('/clientes/%d' % cliente.id)
  else:
    raise PermissionDenied
