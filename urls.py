from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'^findstock/(?P<barcode>[\w\d\-\.]+)/$', 'fly.views.findstock'),
    path(r'^flipnow/(?P<id>\d+)/$', 'fly.views.flipnow'),
    path(r'^printbarcode/(?P<stock_url>\d+)/$', 'fly.views.print_stock_barcode'),
    path(r'^flipbylocation/(?P<loc>\w+)/$', 'fly.views.flipbylocation'),

    path(r'^admin_tools/', include('admin_tools.urls')),
    path(r'^account/', include('django_authopenid.urls')),
    path(r'^', include(admin.site.urls)),
]