from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

from .models import MedicionEnergetica, Usuario, Empleado
from .forms import (
    MedicionForm,
    BuscarMedicionForm,
    ActualizarMedicionForm,
    UsuarioForm,
    EmpleadoForm,
)


def inicio(request):
    return render(request, "inicio.html")

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

def listar_mediciones(request):
    formulario = BuscarMedicionForm(request.GET or None)
    mediciones = MedicionEnergetica.objects.all().order_by('-fecha')

    if formulario.is_valid():
        edificio = formulario.cleaned_data.get("edificio")
        if edificio:
            mediciones = mediciones.filter(edificio__icontains=edificio)

    return render(request, "mediciones_listado.html", {
        "mediciones": mediciones,
        "formulario": formulario,
    })

def ver_medicion(request, pk):
    medicion = get_object_or_404(MedicionEnergetica, pk=pk)
    return render(request, "medicion_detalle.html", {"medicion": medicion})

class ActualizarMedicion(UpdateView):
    model = MedicionEnergetica
    form_class = ActualizarMedicionForm
    template_name = "actualizar_medicion.html"
    success_url = reverse_lazy("listar_mediciones")

class EliminarMedicion(DeleteView):
    model = MedicionEnergetica
    template_name = "eliminar_medicion.html"
    success_url = reverse_lazy("listar_mediciones")

def crear_usuario(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    else:
        formulario = UsuarioForm()

    return render(request, "crear_usuario.html", {"formulario": formulario})


def crear_empleado(request):
    if request.method == "POST":
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    else:
        formulario = EmpleadoForm()

    return render(request, "crear_empleado.html", {"formulario": formulario})
