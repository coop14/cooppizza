from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^clientes/', include('cooppizza.clientes.urls')),
  url(r'^cardapio/', include('cooppizza.cardapio.urls')),
  url(r'^pedidos/', include('cooppizza.pedidos.urls')),
  url(r'^feedback/', include('cooppizza.formFeedback.urls')),
)
