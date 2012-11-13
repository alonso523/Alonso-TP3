# Create your views here.
# coding: utf-8
# Creación de las vistas de la aplicacion

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from contactos.models import Contacto           #IMporta el modelo contacto
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.core.context_processors import csrf

def index(request):
	lista_contactos = Contacto.objects.all().order_by('apellido1')
	context   = {'lista_contactos': lista_contactos}
	return render(request, 'contactos/index.html', context)

#Detalle del contacto
def detalle(request, contacto_id):
	contacto = get_object_or_404(Contacto, pk=contacto_id)
	return render(request, 'contactos/detalle.html', {'contacto': contacto})

#Función que agrega un contacto a la lista de contactos
#def agregar(request):
#	return render(request, 'contactos/agregar.html')

#Funcion que agrega un contacto
def agregar(request):
	ContactoFormSet = modelformset_factory(Contacto)
	if request.method == 'POST':
		formset = ContactoFormSet(request.POST, request.FILES,
		                        queryset=Contacto.objects.filter(nombre__startswith='O'))
        	if formset.is_valid():
			formset.save()
			return HttpResponseRedirect('/contactos/')
	else:
        	formset = ContactoFormSet(queryset=Contacto.objects.filter(nombre__startswith='O'))
		context = {'formset': formset}
    	return render_to_response('contactos/agregar.html', context, context_instance=RequestContext(request))
	
