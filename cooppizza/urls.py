from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^clientes/', include('clientes.urls')),
  url(r'^cardapio/', include('cardapio.urls')),
  url(r'^pedidos/', include('pedidos.urls')),
)
