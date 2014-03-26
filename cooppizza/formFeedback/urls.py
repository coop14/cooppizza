from django.conf.urls import patterns, include, url
from formFeedback import views
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', views.formularioFeedback, name='formularioFeedback'),
	url(r'^base$', views.base, name='base'),
)