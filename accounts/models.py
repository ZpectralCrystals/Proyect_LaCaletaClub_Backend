from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    dni = models.CharField(max_length=8)
    avatar_url = models.TextField(null=True, blank=True)
    puntos = models.BigIntegerField(default=0)
    role = models.IntegerField(default=1)  # rol personalizado: 1, 2, 3, 4, 5

    def __str__(self):
        return f'Perfil de {self.user.username}'
