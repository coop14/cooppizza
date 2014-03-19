from django.conf.urls import patterns, include, url

from django.contrib import admin
from produto import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'promo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^produto/', include('produto.urls')),
)
