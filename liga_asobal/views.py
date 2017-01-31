from django.shortcuts import render, get_object_or_404
from liga_asobal.models import Equipo, Jugador, Arbitro, Partido

# Create your views here.

def index(request):
	return render(request, 'liga_asobal/index.html')

def lista_equipos(request):
	template_name = 'liga_asobal/lista_equipos.html'
	equipos = Equipo.objects.all()
	contexto = {'equipos':equipos}
	return render(request, template_name, contexto )

def lista_jugadores(request):
	template_name = 'liga_asobal/lista_jugadores.html'
	jugadores = Jugador.objects.all()
	contexto = {'jugadores':jugadores}
	return render(request, template_name, contexto)

def lista_arbitros(request):
	template_name = 'liga_asobal/lista_arbitros.html'
	arbitros = Arbitro.objects.all()
	contexto = {'arbitros':arbitros}
	return render(request, template_name, contexto)

def lista_partidos(request):
	template_name = 'liga_asobal/lista_partidos.html'
	partidos = Partido.objects.all()
	contexto = {'partidos':partidos}
	return render(request, template_name, contexto)	

def detalles_equipos(request, id):
	template_name = 'liga_asobal/detalles_equipos.html'
	if request.method == 'GET':
		equipo = get_object_or_404(Equipo, pk = id)
		contexto = { 'equipo' : equipo }
		if not equipo:
			return redirect(reverse('liga_asobal:lista_equipos'))
		return render(request, template_name, contexto)

def detalles_jugadores(request, id):
	template_name = 'liga_asobal/detalles_jugadores.html'
	if request.method == 'GET':
		jugador = get_object_or_404(Jugador, pk = id)
		contexto = { 'jugador' : jugador }
		if not jugador:
			return redirect(reverse('liga_asobal:lista_jugadores'))
		return render(request, template_name, contexto)

def detalles_arbitros(request, id):
	template_name = 'liga_asobal/detalles_arbitros.html'
	if request.method == 'GET':
		arbitro = get_object_or_404(Arbitro, pk = id)
		contexto = { 'arbitro' : arbitro }
		if not arbitro:
			return redirect(reverse('liga_asobal:lista_arbitros'))
		return render(request, template_name, contexto)
