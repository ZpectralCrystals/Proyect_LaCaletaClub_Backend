# descuentos/models.py
from django.db import models
from categories.models import Categoria  # Asegúrate de tener esta app y modelo
from products.models import Producto  # Asegúrate de tener esta app y modelo

class Descuento(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    descuento = models.PositiveIntegerField(null=True, blank=True)
    dia = models.IntegerField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.TextField(null=True, blank=True)
    type = models.SmallIntegerField(choices=[(1, 'Evento'), (2, 'Descuento')], null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    isActive = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = 'descuentostab'

    def __str__(self):
        return self.name
