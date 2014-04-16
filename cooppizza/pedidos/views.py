from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied

def web(request):
  if 'id' in request.COOKIES:
    cookie_id = request.COOKIES['id']
    return HttpResponse('Got cookie with id=%s' % cookie_id)
  else:
    resp = HttpResponse('No id cookie! Sending cookie to client')
    resp.set_cookie('id', 'some_value_99')
    return resp

def index(request):
  if 'id' in request.COOKIES:
    cookie_id = request.COOKIES['id']
    return HttpResponse('Got cookie with id=%s' % cookie_id)
  else:
    resp = HttpResponse('No id cookie! Sending cookie to client')
    resp.set_cookie('id', 'some_value_99')
    return resp

def pedidoLista(request):
  template = loader.get_template('pedidos/index.html')
  return HttpResponse(template.render(RequestContext(request)))

def pedidoNovo(request):
  if 'id' in request.COOKIES:
    cookie_id = request.COOKIES['id']
    return HttpResponse('Got cookie with id=%s' % cookie_id)
  else:
    resp = HttpResponse('No id cookie! Sending cookie to client')
    resp.set_cookie('id', 'some_value_99')
    return resp
