from django import forms
from .models import MedicionEnergetica, Usuario, Empleado


class MedicionForm(forms.ModelForm):
    class Meta:
        model = MedicionEnergetica
        fields = [
            "edificio",
            "equipo",
            "potencia_kw",
            "energia_kwh",
            "ubicacion",
            "descripcion",
            "imagen",
        ]


#class MedicionForm(forms.Form):
 #   edificio = forms.CharField(max_length=80, label="Lugar (edificio)")
  #  equipo   = forms.CharField(max_length=80, label="Qué se quiere medir (equipo)")

class BuscarMedicionForm(forms.Form):
    edificio = forms.CharField(
        max_length=80,
        required=False,
        label="Buscar por edificio"
    )

class ActualizarMedicionForm(forms.ModelForm):
    class Meta:
        model = MedicionEnergetica
        fields = ["edificio", "equipo", "ubicacion"]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre", "email"]


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ["nombre", "rol"]
