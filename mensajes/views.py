from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Mensaje
from .forms import MensajeForm


@login_required
def bandeja_entrada(request):
    """Mensajes recibidos."""
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by("-creado")
    return render(request, "mensajes/bandeja_entrada.html", {
        "mensajes": mensajes
    })


@login_required
def mensajes_enviados(request):
    """Mensajes enviados."""
    mensajes = Mensaje.objects.filter(remitente=request.user).order_by("-creado")
    return render(request, "mensajes/enviados.html", {
        "mensajes": mensajes
    })


@login_required
def detalle_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)

    # Permitir ver solo si soy remitente o destinatario
    if mensaje.destinatario != request.user and mensaje.remitente != request.user:
        return redirect("bandeja_entrada")

    # Marcar como leído
    if mensaje.destinatario == request.user and not mensaje.leido:
        mensaje.leido = True
        mensaje.save()

    return render(request, "mensajes/detalle.html", {
        "mensaje": mensaje
    })


@login_required
def enviar_mensaje(request):
    """Enviar mensaje."""
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.remitente = request.user
            nuevo.save()
            return redirect("bandeja_entrada")
    else:
        form = MensajeForm()

    return render(request, "mensajes/enviar.html", {
        "form": form
    })

@login_required
def detalle_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    return render(request, "mensajes/detalle.html", {"mensaje": mensaje})
