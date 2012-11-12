# Create your views here.
# coding: utf-8
# Creación de las vistas de la aplicacion

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from contactos.models import Contacto

def index(request):
	return render(request, 'contactos/index.html')
