# recomendaciones/models.py
from django.db import models
from django.contrib.auth.models import User  # Importar correctamente User
from accounts.models import Profile  # Asegúrate de que el modelo Profile esté bien importado

class Recomendaciones(models.Model):
    description = models.TextField()
    isActive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Recomendación de {self.userid}'

    class Meta:
        db_table = 'recomendaciones'
