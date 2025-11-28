from django import forms
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["avatar", "bio", "link", "fecha_nacimiento"]


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
