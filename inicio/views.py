from django.shortcuts import render
from django.utils import timezone
from .models import MedicionEnergetica

def inicio(request):
    return render(request, "inicio.html")

def crear_medicion(request, edificio, equipo):
    medicion = MedicionEnergetica.objects.create(
        edificio=edificio,
        equipo=equipo,
        fecha=timezone.now(),
        potencia_kw=0,
        energia_kwh=0,
        ubicacion=""
    )
    return render(request, "crear_medicion.html", {"medicion": medicion})

def listar_mediciones(request):
    mediciones = MedicionEnergetica.objects.order_by('-fecha')
    return render(request, "mediciones_listado.html", {"mediciones": mediciones})



