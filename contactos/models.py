from django.db import models

# Create your models here.
# Modelo contacto, el cual tiene todos los datos de los contactos

class Contacto(models.Model):

	nombre    =  models.CharField(max_length=200)
	apellido1 =  models.CharField(max_length=200)
	apellido2 =  models.CharField(max_length=200)
	edad      =  models.IntegerField()
	telefono  =  models.IntegerField()
	correo    =  models.EmailField(max_length=200, unique = True)
	direccion =  models.FloatField()
	
	def __unicode__(self):
		return self.nombre

	def __unicode__(self):
		return self.apellido1

	def __unicode__(self):
		return self.apellido2

	def __unicode__(self):
		return self.edad

	def __unicode__(self):
		return self.telefono

	def __unicode__(self):
		return self.correo

