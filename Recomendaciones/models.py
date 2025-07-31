from django.db import models
from accounts.models import Profile  # Asegúrate de que esto esté bien importado

class Recomendaciones(models.Model):
    description = models.TextField()
    isActive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    userid = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Recomendación de {self.userid}'

    class Meta:
        db_table = 'recomendaciones'