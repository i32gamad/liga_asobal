from django.contrib import admin
from liga_asobal.models import Equipo, Jugador, Partido, Arbitro

# Register your models here.

admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Partido)
admin.site.register(Arbitro)
