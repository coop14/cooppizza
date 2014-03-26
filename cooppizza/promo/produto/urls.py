from django.conf.urls import patterns, url

from produto import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^listar$', views.promoListar, name='promoListar'),
	url(r'^(?P<produto_id>\d+)/$', views.promoConsultar, name='promoConsultar'),
	url(r'^(?P<produto_id>\d+)/editar$', views.promoEditar, name='promoEditar'),
	url(r'^(?P<produto_id>\d+)/excluir$', views.promoExcluir, name='promoExcluir'),
)