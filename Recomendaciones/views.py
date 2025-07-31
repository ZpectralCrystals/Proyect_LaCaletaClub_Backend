# views.py
from rest_framework import viewsets
from .models import Recomendaciones
from .serializer import RecomendacionSerializer

class RecomendacionViewSet(viewsets.ModelViewSet):
    queryset = Recomendaciones.objects.all().order_by('-created_at')
    serializer_class = RecomendacionSerializer
