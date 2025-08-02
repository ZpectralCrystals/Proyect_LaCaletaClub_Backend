# blogs/models.py
from django.db import models
from django.contrib.auth.models import User  # Importar User de Django
from products.models import Producto  # Asegúrate de tener esta app y modelo

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Referencia a User
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Blog de {self.titulo}'

    class Meta:
        db_table = 'blogs'  # Nombre exacto de la tabla
