from django.conf.urls import patterns, include, url
from cooppizza.formFeedback import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^form$', views.formularioFeedback, name='formularioFeedback'),
)