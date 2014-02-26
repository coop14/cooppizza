from django.conf.urls import patterns, url
from clientes import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^novo$', views.clienteNovo, name='wtf0'),
  url(r'^consulta$', views.clienteConsulta, name='wtf1'),
  url(r'^adicionar$', views.clienteAdicionar, name='wtf2'),
  url(r'^(?P<cliente_id>\d+)$', views.clienteDados, name='wtf3'),
  url(r'^(?P<cliente_id>\d+)/enderecos/novo$', views.enderecoNovo, name='wtf4'),
  url(r'^(?P<cliente_id>\d+)/enderecos/adicionar$', views.enderecoAdicionar, name='wtf5'),
  url(r'^(?P<cliente_id>\d+)/enderecos/deletar/(?P<endereco_id>\d+)$', views.enderecoDeletar, name='wtf6'),
)
