from django.db import models
from categorias.models import Categoria  # Asegúrate de tener esta app y modelo

class Producto(models.Model):
    name = models.TextField()
    type = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    varietyOptions = models.JSONField(null=True, blank=True)
    isActive = models.BooleanField(null=True, blank=True)
    isFavorite = models.BooleanField(default=True)

    def __str__(self):
        return self.name
