from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Equipo(models.Model):
	nombre_equipo = models.CharField(max_length=70)
	escudo = models.ImageField(upload_to='static/img/')
	partidos_ganados = models.IntegerField()
	partidos_perdidos = models.IntegerField()
	partidos_empatados = models.IntegerField()
	puntos = models.IntegerField()

	def __str__(self):
		return self.nombre_equipo

class Jugador(models.Model):
	nombre_jugador = models.CharField(max_length=70)
	posicion = models.CharField(max_length=70)
	equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
	nacionalidad = models.CharField(max_length=50)
	edad = models.IntegerField()

	def __str__(self):
		return self.nombre_jugador

class Arbitro(models.Model):
	nombre_arbitro = models.CharField(max_length=70)
	edad = models.IntegerField()

	def __str__(self):
		return self.nombre_arbitro

class Partido(models.Model):
	equipo_local = models.ForeignKey(Equipo, related_name = 'equipo_local', on_delete=models.CASCADE)
	equipo_visitante = models.ForeignKey(Equipo, related_name = 'equipo_visitante', on_delete=models.CASCADE)
	arbitro = models.ForeignKey(Arbitro, on_delete=models.CASCADE)									
	goles_local = models.IntegerField()
	goles_visitante = models.IntegerField()
	fecha_partido = models.DateTimeField('date published')
	
	
	def __str__(self):
		return self.equipo_local.nombre_equipo