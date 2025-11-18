from django.urls import path
from .views import inicio, crear_medicion, listar_mediciones, ver_medicion

urlpatterns = [
    path("", inicio, name="inicio"),
    path("crear-medicion/", crear_medicion, name="crear_medicion"),
    path("mediciones/", listar_mediciones, name="listar_mediciones"),
    path("mediciones/<int:pk>/", ver_medicion, name="ver_medicion"),
]

