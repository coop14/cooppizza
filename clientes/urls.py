from django.conf.urls import patterns, url
from clientes import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^consulta$', views.consulta, name='wtf1'),
  url(r'^(?P<cliente_id>\d+)$', views.dados, name='wtf2'),
  url(r'^(?P<cliente_id>\d+)/enderecos/novo$', views.enderecoNovo, name='wtf3'),
  url(r'^(?P<cliente_id>\d+)/enderecos/adicionar$', views.enderecoAdicionar, name='wtf4'),
  url(r'^(?P<cliente_id>\d+)/enderecos/deletar/(?P<endereco_id>\d+)$', views.enderecoDeletar, name='wtf5'),
)
