from django.db import models

class MedicionEnergetica(models.Model):
    edificio = models.CharField(max_length=80)
    equipo = models.CharField(max_length=80, blank=True)
    fecha = models.DateTimeField()
    potencia_kw = models.DecimalField(max_digits=8, decimal_places=3)
    energia_kwh = models.DecimalField(max_digits=10, decimal_places=3)
    ubicacion = models.CharField(max_length=120, blank=True)

    class Meta:
        verbose_name = "Medición energética"
        verbose_name_plural = "Mediciones energéticas"

    def __str__(self):
        return f"#{self.id} - {self.edificio} ({self.equipo})"


class Usuario(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombre = models.CharField(max_length=80)
    rol = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.rol})"


    
