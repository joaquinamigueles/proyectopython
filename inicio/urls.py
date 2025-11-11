from django.urls import path
from inicio.views import inicio, crear_medicion, listar_mediciones

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-medicion/<edificio>/<equipo>/', crear_medicion, name='crear_medicion'),
    path('mediciones/', listar_mediciones, name='listar_mediciones'),
]

