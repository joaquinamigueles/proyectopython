from django.urls import path
from .views import (
    iniciar_sesion,
    registrar_usuario,
    perfil,
    cerrar_sesion,
    editar_perfil,
    cambiar_password,
)

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registrar/', registrar_usuario, name='registrar'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-password/', cambiar_password, name='cambiar_password'),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
]
