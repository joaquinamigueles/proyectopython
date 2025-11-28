from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import MedicionEnergetica
from .forms import MedicionForm
from django.views.generic import ListView, UpdateView, DeleteView, TemplateView

class ListaMediciones(ListView):
    model = MedicionEnergetica
    template_name = "mediciones_listado.html"
    context_object_name = "mediciones"
    ordering = ['-fecha']


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

class AboutView(TemplateView):
    template_name = "about.html"

@login_required   
def crear_medicion(request):
    if request.method == "POST":
        form = MedicionForm(request.POST, request.FILES)
        if form.is_valid():
            medicion = form.save(commit=False)
            medicion.fecha = timezone.now()
            medicion.save()
            return redirect("listar_mediciones")
    else:
        form = MedicionForm()

    return render(request, "crear_medicion.html", {"form": form})

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

class ActualizarMedicion(LoginRequiredMixin, UpdateView):
    model = MedicionEnergetica
    form_class = MedicionForm
    template_name = "actualizar_medicion.html"
    success_url = reverse_lazy("listar_mediciones")


class EliminarMedicion(LoginRequiredMixin, DeleteView):
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


class ListaMediciones(ListView):
    model = MedicionEnergetica
    template_name = "mediciones_listado.html"
    context_object_name = "mediciones"
    ordering = ["-fecha"]

class ActualizarMedicion(LoginRequiredMixin, UpdateView):  
    model = MedicionEnergetica
    template_name = "actualizar_medicion.html"
    fields = ["edificio", "equipo", "potencia_kw", "energia_kwh", "ubicacion"]
    success_url = reverse_lazy("listar_mediciones")

class EliminarMedicion(LoginRequiredMixin, DeleteView):   
    model = MedicionEnergetica
    template_name = "eliminar_medicion.html"
    success_url = reverse_lazy("listar_mediciones")

