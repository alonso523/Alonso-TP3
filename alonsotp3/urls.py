from django.conf.urls import patterns, include, url
from contactos.views import index, agregar, detalle, editar, eliminar, actualizar, buscar

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
    #url(r'auth/', include('social_auth.urls')),
    url(r'^contactos/$', index),
    url(r'^contactos/agregar/$', agregar),
    url(r'^contactos/detalle/$', detalle),
    url(r'^contactos/(?P<contacto_id>\d+)/$', detalle),
    url(r'^contactos/editar/(?P<contacto_id>\d+)/$', editar),
    url(r'^contactos/editar/$', editar),
    url(r'^contactos/eliminar/(?P<contacto_id>\d+)/$', eliminar),
    url(r'^contactos/actualizar/(?P<contacto_id>\d+)/$', actualizar),
    url(r'^social/actualizar/(?P<contacto_id>\d+)/$', actualizar),
    url(r'^contactos/buscar/$', buscar),
    #url(r'^search/$', views.search),
)
