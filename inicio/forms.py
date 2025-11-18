from django import forms

class MedicionForm(forms.Form):
    edificio = forms.CharField(max_length=80, label="Lugar (edificio)")
    equipo   = forms.CharField(max_length=80, label="Qué se quiere medir (equipo)")

class BuscarMedicionForm(forms.Form):
    edificio = forms.CharField(
        max_length=80,
        required=False,
        label="Buscar por edificio"
    )
