from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('baseMod',
    # Examples:
    # url(r'^$', 'pinteArg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', 'views.inicio'),
    url(r'^admin/', include(admin.site.urls)),
)
