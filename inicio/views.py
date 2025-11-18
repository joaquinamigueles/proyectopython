from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import MedicionEnergetica
from .forms import MedicionForm, BuscarMedicionForm   

def inicio(request):
    return render(request, "inicio.html")

# ------- CREAR MEDICIÓN (con formulario) -------
def crear_medicion(request):
    if request.method == "POST":
        formulario = MedicionForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            MedicionEnergetica.objects.create(
                edificio=datos["edificio"],
                equipo=datos["equipo"],
                fecha=timezone.now(),
                potencia_kw=0,
                energia_kwh=0,
                ubicacion=""
            )
            return redirect("listar_mediciones")
    else:
        formulario = MedicionForm()

    return render(request, "crear_medicion.html", {"formulario": formulario})

# ------- LISTAR + BUSCAR MEDICIONES -------
def listar_mediciones(request):
    formulario = BuscarMedicionForm(request.GET or None)
    mediciones = MedicionEnergetica.objects.all().order_by('-fecha')

    if formulario.is_valid():
        edificio = formulario.cleaned_data.get("edificio")
        if edificio:
            mediciones = mediciones.filter(edificio__icontains=edificio)

    contexto = {
        "mediciones": mediciones,
        "formulario": formulario,
    }
    return render(request, "mediciones_listado.html", contexto)

# ------- VER DETALLE -------
def ver_medicion(request, pk):
    medicion = get_object_or_404(MedicionEnergetica, pk=pk)
    return render(request, "medicion_detalle.html", {"medicion": medicion})
