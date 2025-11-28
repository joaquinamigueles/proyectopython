from django.urls import path
from .views import (
    bandeja_entrada,
    enviar_mensaje,
    mensajes_enviados,
    detalle_mensaje,
)

urlpatterns = [
    path("", bandeja_entrada, name="bandeja_entrada"),
    path("enviar/", enviar_mensaje, name="enviar_mensaje"),
    path("enviados/", mensajes_enviados, name="mensajes_enviados"),
    path("<int:pk>/", detalle_mensaje, name="ver_mensaje"),
]
