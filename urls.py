from django.conf.urls.defaults import patterns, include, url
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^findstock/(?P<barcode>[\w\d\-\.]+)/$', 'fly.views.findstock'),
    (r'^flipnow/(?P<id>\d+)/$', 'fly.views.flipnow'),
    (r'^duplicate/(?P<id>\d+)/$', 'fly.views.duplicate'),
    (r'^printbarcode/(?P<stock_url>\d+)/$', 'fly.views.print_stock_barcode'),
    (r'^flipbylocation/(?P<loc>\w+)/$', 'fly.views.flipbylocation'),

    url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^account/', include('django_authopenid.urls')),
    (r'^', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
