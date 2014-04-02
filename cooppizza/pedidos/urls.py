from django.conf.urls import patterns, url
from cooppizza.pedidos import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^web$', views.web, name='web'), # WEB
  url(r'^lista$', views.pedidoLista, name='pedidoLista'),
  url(r'^novo$', views.pedidoNovo, name='pedidoNovo'),
)
