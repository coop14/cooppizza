from django.conf.urls import patterns, url
from pedidos import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^web$', views.web, name='web'), # WEB
)
