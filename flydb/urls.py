from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'^findstock/(?P<barcode>[\w\d\-\.]+)/$', 'flydb.views.findstock'),
    path(r'^flipnow/(?P<id>\d+)/$', 'flydb.views.flipnow'),
    path(r'^printbarcode/(?P<stock_url>\d+)/$', 'flydb.views.print_stock_barcode'),
    path(r'^flipbylocation/(?P<loc>\w+)/$', 'flydb.views.flipbylocation'),

    path(r'^admin_tools/', include('admin_tools.urls')),
    path(r'^account/', include('django_authopenid.urls')),
    path(r'^', include(admin.site.urls)),
]