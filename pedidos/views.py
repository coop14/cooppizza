from django.shortcuts import render

def index(request):
  template = loader.get_template('pedidos/index.html')
  return HttpResponse(template.render(RequestContext(request)))
