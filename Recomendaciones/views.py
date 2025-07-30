from rest_framework import viewsets
from .models import Recomendaciones
from .serializers import RecomendacionSerializer

class RecomendacionViewSet(viewsets.ModelViewSet):
    queryset = Recomendaciones.objects.all().order_by('-fecha_creacion')
    serializer_class = RecomendacionSerializer
