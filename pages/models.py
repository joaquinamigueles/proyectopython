from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150, blank=True)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to="pages", blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
