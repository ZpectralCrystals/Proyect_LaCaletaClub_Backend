# anuncios/models.py
from django.db import models

class Anuncio(models.Model):
    titulo = models.TextField(null=False)
    mensaje = models.TextField(null=True, blank=True)
    imagen = models.TextField(null=True, blank=True)
    activo = models.BooleanField(null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'anuncios'  # Nombre exacto de la tabla
