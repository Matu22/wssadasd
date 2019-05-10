from django.db import models

# Create your models here.

class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=100)
	ESTADO_CHOICES = (
		('DISPONIBLE', 'Disponible'),
		('NO DISPONIBLE', 'No Disponible'),
		)
	estado = models.CharField(max_length = 15, choices = ESTADO_CHOICES)