from django.conf.urls import patterns, url

from cooppizza.promocao import views

urlpatterns = patterns('',
    url(r'^$', views.promoIndex, name='promoIndex'),
	url(r'^listar$', views.promoListar, name='promoListar'),
	url(r'^criar$', views.promoCriar, name='promoCriar'),
	url(r'^adicionar$', views.promoAdicionar, name='promoAdicionar'),
	url(r'^(?P<promocao_id>\d+)/$', views.promoConsultar, name='promoConsultar'),
	url(r'^(?P<promocao_id>\d+)/editar$', views.promoEditar, name='promoEditar'),
	url(r'^(?P<promocao_id>\d+)/excluir$', views.promoExcluir, name='promoExcluir'),
)