# blogs/views.py
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated

class BlogPublicView(generics.ListAPIView):
    queryset = Blog.objects.filter(isActive=True)
    serializer_class = BlogSerializer



# views.py (Django)
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated

# views.py (Django)
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated

class BlogAdminView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados

    def perform_create(self, serializer):
        # Asignar el usuario autenticado al campo 'user'
        serializer.save(user=self.request.user)  # Asignar el usuario que hizo la solicitud

class BlogAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]  # Solo accesible por usuarios autenticados
