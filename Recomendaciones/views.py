# recomendaciones/views.py
from rest_framework import generics
from .models import Recomendaciones
from .serializers import RecomendacionesSerializer
from rest_framework.permissions import IsAuthenticated


class RecomendacionesPublicView(generics.ListAPIView):
    queryset = Recomendaciones.objects.filter(isActive=True)
    serializer_class = RecomendacionesSerializer



class RecomendacionesAdminView(generics.ListCreateAPIView):
    queryset = Recomendaciones.objects.all()
    serializer_class = RecomendacionesSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados

class RecomendacionesAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recomendaciones.objects.all()
    serializer_class = RecomendacionesSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados
