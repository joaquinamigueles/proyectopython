from django.contrib import admin
from .models import MedicionEnergetica

@admin.register(MedicionEnergetica)
class MedicionEnergeticaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "edificio", "equipo", "potencia_kw", "energia_kwh", "ubicacion")
    list_filter = ("edificio", "equipo")
    search_fields = ("edificio", "equipo", "ubicacion")
    ordering = ("-fecha",)
