from django.conf.urls import patterns, include, url
from cooppizza.formFeedback import views

urlpatterns = patterns('',
	url(r'^$', views.indexFeedback, name='indexFeedback'),
	url(r'^form$', views.formularioFeedback, name='formularioFeedback'),
	url(r'^form/obrigado$', views.obrigado, name='obrigado'),
)