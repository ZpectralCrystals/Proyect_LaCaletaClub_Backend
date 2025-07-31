from django.db import models

class Recomendaciones(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo