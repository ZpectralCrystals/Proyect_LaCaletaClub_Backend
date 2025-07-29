from django.db import models

class Categoria(models.Model):
    descripcion = models.TextField()
    isActive = models.BooleanField(null=True, default=True)
    icon = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'categoriatab'

    def __str__(self):
        return self.descripcion
