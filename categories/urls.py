# categories/urls.py
from django.urls import path
from .views import CategoriaPublicView, CategoriaAdminView, CategoriaAdminDetailView

urlpatterns = [
    # Vista pública: solo GET
    path('public/categorias/', CategoriaPublicView.as_view(), name='categoria-public-list'),
    
    # Vista de admin: GET, POST, PATCH, DELETE
    path('categorias/', CategoriaAdminView.as_view(), name='categoria-admin-list'),
    path('categorias/<int:pk>/', CategoriaAdminDetailView.as_view(), name='categoria-admin-detail'),
]
