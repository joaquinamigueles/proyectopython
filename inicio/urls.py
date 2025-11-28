from django.urls import path
from .views import (
    inicio,
    crear_medicion,
    ListaMediciones,  
    ver_medicion,
    ActualizarMedicion,
    EliminarMedicion,
    crear_usuario,
    crear_empleado,
    AboutView,
)

urlpatterns = [
    path("", inicio, name="inicio"),
    path("about/", AboutView.as_view(), name="about"),   # 👈 FALTABA ESTA

    path("crear-medicion/", crear_medicion, name="crear_medicion"),
    path("mediciones/", ListaMediciones.as_view(), name="listar_mediciones"),
    path("mediciones/<int:pk>/", ver_medicion, name="ver_medicion"),
    path("mediciones/<int:pk>/actualizar/", ActualizarMedicion.as_view(), name="actualizar_medicion"),
    path("mediciones/<int:pk>/eliminar/", EliminarMedicion.as_view(), name="eliminar_medicion"),

    path("usuarios/nuevo/", crear_usuario, name="crear_usuario"),
    path("empleados/nuevo/", crear_empleado, name="crear_empleado"),

    path("pages/", ListaMediciones.as_view(), name="pages_list"),
    path("pages/<int:pk>/", ver_medicion, name="page_detail"),
]
