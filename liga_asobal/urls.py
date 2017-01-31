from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^equipos/$', views.lista_equipos, name="lista_equipos"),
    url(r'^jugadores/$', views.lista_jugadores, name="lista_jugadores"),
    url(r'^arbitros/$', views.lista_arbitros, name="lista_arbitros"),
   	url(r'^partidos/$', views.lista_partidos, name="lista_partidos"),
   	url(r'equipo/detalle/(?P<id>[0-9]+)/$', views.detalles_equipos, name = 'detalles_equipos'),
   	url(r'jugador/detalle/(?P<id>[0-9]+)/$', views.detalles_jugadores, name = 'detalles_jugadores'),
	url(r'arbitro/detalle/(?P<id>[0-9]+)/$', views.detalles_arbitros, name = 'detalles_arbitros'),
	

]