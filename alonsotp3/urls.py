from django.conf.urls import patterns, include, url
from contactos.views import index, agregar, detalle

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alonsotp3.views.home', name='home'),
    # url(r'^alonsotp3/', include('alonsotp3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^contactos/$', index),
    url(r'^contactos/agregar/$', agregar),
    url(r'^contactos/detalle/$', detalle),
    #url(r'^contactos/', include('contactos.urls')),
    url(r'^contactos/(?P<contacto_id>\d+)/$', detalle),
    #url(r'^search/$', views.search),
)
