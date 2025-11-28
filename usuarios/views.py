from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import PerfilForm, RegistroForm
from .models import Perfil


def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("inicio")
    else:
        form = AuthenticationForm()
    return render(request, "usuarios/iniciar_sesion.html", {"form": form})


def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("inicio")
    else:
        form = RegistroForm()
    return render(request, "usuarios/registrar.html", {"form": form})


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")


@login_required
def perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, "usuarios/perfil.html", {"perfil": perfil})


@login_required
def editar_perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect("perfil")
    else:
        form = PerfilForm(instance=perfil)
    return render(request, "usuarios/editar_perfil.html", {"form": form})


@login_required
def cambiar_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("perfil")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "usuarios/cambiar_password.html", {"form": form})
