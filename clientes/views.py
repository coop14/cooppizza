from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse
#from django.http.response import HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.template import RequestContext, loader

from clientes.models import Cliente

def index(request):
  template = loader.get_template('clientes/index.html')
  return HttpResponse(template.render(RequestContext(request)))

def consulta(request):
  if request.method == 'POST':
    try:
      cliente = Cliente.objects.get(email=request.POST['email'])
    except (Cliente.DoesNotExist):
      raise Http404
      #return HttpResponseNotFound()
    else:
      return redirect('/clientes/%d' % cliente.id)
  else:
    raise PermissionDenied
    #return HttpResponseForbidden()

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
