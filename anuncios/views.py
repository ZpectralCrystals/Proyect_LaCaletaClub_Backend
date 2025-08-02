# anuncios/views.py
from rest_framework import generics
from .models import Anuncio
from .serializers import AnuncioSerializer
from rest_framework.permissions import IsAuthenticated


class AnuncioPublicView(generics.ListAPIView):
    queryset = Anuncio.objects.filter(activo=True)
    serializer_class = AnuncioSerializer



class AnuncioAdminView(generics.ListCreateAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados

class AnuncioAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados
