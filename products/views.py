# products/views.py
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class ProductoPublicView(generics.ListAPIView):
    queryset = Producto.objects.filter(isActive=True)
    serializer_class = ProductoSerializer



class ProductoAdminView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados

class ProductoAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados
