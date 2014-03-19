from django.conf.urls import patterns, url
from clientes import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^web$', views.web, name='web'), # WEB
  url(r'^acesso$', views.webAcesso, name='webAcesso'), # WEB
  url(r'^novo$', views.clienteNovo, name='clienteNovo'),
  url(r'^consulta$', views.clienteConsulta, name='clienteConsulta'),
  url(r'^adicionar$', views.clienteAdicionar, name='clienteAdicionar'),
  url(r'^lista$', views.clienteLista, name='clienteLista'),
  url(r'^(?P<cliente_id>\d+)$', views.clienteDados, name='clienteDados'),
  url(r'^(?P<cliente_id>\d+)/enderecos/novo$', views.enderecoNovo, name='enderecoNovo'),
  url(r'^(?P<cliente_id>\d+)/enderecos/adicionar$', views.enderecoAdicionar, name='enderecoAdicionar'),
  url(r'^(?P<cliente_id>\d+)/enderecos/deletar/(?P<endereco_id>\d+)$', views.enderecoDeletar, name='enderecoDeletar'),
)
