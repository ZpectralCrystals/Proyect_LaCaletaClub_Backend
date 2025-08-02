# categories/views.py
from rest_framework import generics
from .models import Categoria
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from .models import Categoria
from .serializer import CategoriaSerializer

class CategoriaPublicView(generics.ListAPIView):
    queryset = Categoria.objects.filter(isActive=True)
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]


class CategoriaAdminView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados

class CategoriaAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados
