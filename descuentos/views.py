# descuentos/views.py
from rest_framework import generics
from .models import Descuento
from .serializers import DescuentoSerializer
from rest_framework.permissions import IsAuthenticated


class DescuentoPublicView(generics.ListAPIView):
    queryset = Descuento.objects.filter(isActive=True)
    serializer_class = DescuentoSerializer

class DescuentoAdminView(generics.ListCreateAPIView):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados

    def perform_create(self, serializer):
        user = self.request.user  # Aquí verificamos el usuario
        print(f"Usuario autenticado: {user}")
        serializer.save()
class DescuentoAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados
