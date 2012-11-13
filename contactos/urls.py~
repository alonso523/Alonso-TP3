from django.conf.urls import patterns, include, url
from contactos.models import Contacto

urlpatterns = patterns('contactos.views',
    url(r'^$', 'index'),
    url(r'^(?P<contacto_id>\d+)/$', 'detalle'),
