from django.urls import path
from .views import (
    inicio,
    crear_medicion,
    listar_mediciones,
    ver_medicion,
    ActualizarMedicion,
    EliminarMedicion,
)

urlpatterns = [
    path("", inicio, name="inicio"),
    path("crear-medicion/", crear_medicion, name="crear_medicion"),
    path("mediciones/", listar_mediciones, name="listar_mediciones"),
    path("mediciones/<int:pk>/", ver_medicion, name="ver_medicion"),
    path("mediciones/<int:pk>/actualizar/", ActualizarMedicion.as_view(), name="actualizar_medicion"),
    path("mediciones/<int:pk>/eliminar/", EliminarMedicion.as_view(), name="eliminar_medicion"),
]
