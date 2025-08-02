from django.db import models
from accounts.models import Profile
from productos.models import Producto

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)  # 👈 CAMBIO


    def __str__(self):
        return f'Blog de {self.titulo}'

  
