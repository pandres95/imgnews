from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'login/', 'baseMod.views.login_', name='Login'),
    url(r'logout/', 'baseMod.views.logout_', name='Logout'),
    url(r'index.html', 'baseMod.views.inicio', name='Inicio'),
    url('', 'baseMod.views.inicio'),
)
