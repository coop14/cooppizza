from django.shortcuts import render

def web(request):
  template = loader.get_template('pedidos/indexWeb.html')
  return HttpResponse(template.render(RequestContext(request)))

def index(request):
  template = loader.get_template('pedidos/index.html')
  return HttpResponse(template.render(RequestContext(request)))
