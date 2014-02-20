from django.conf.urls import patterns, url
from clientes import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<cliente_id>\d+)$', views.dados, name='wtf2'),
  url(r'^consulta$', views.consulta, name='wtf1'),
  url(r'^alterar/(?P<cliente_id>\d+)$', views.dados, name='wtf2'),
)
