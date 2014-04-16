from django.conf.urls import patterns, include, url
from cooppizza.pedidos import views

urlpatterns = patterns('',
  	url(r'^$', views.indexPedido, name='indexPedido'),
  	url(r'^pizzas$', views.pizzasPedido, name='pizzasPedido'),
  	url(r'^bebidas$', views.bebidasPedido, name='bebidasPedido'),
  	url(r'^bebidas/adiciona/(?P<bebida_id>\d+)$', views.bebidaAdiciona, name='bebidaAdiciona'),
  	url(r'^carrinho/(?P<produto_id>\d+)$', views.carrinhoPedido, name='carrinhoPedido'),
)
