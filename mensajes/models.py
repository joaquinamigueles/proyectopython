from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(
        User,
        related_name='mensajes_enviados',
        on_delete=models.CASCADE
    )
    destinatario = models.ForeignKey(
        User,
        related_name='mensajes_recibidos',
        on_delete=models.CASCADE
    )
    asunto = models.CharField(max_length=100)
    cuerpo = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asunto} ({self.remitente} → {self.destinatario})"

