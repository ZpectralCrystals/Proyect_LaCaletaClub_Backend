# products/urls.py
from django.urls import path
from .views import ProductoPublicView, ProductoAdminView, ProductoAdminDetailView

urlpatterns = [
    # Vista pública: solo GET
    path('public/productos/', ProductoPublicView.as_view(), name='producto-public-list'),
    
    # Vista de admin: GET, POST, PATCH, DELETE
    path('productos/', ProductoAdminView.as_view(), name='producto-admin-list'),
    path('productos/<int:pk>/', ProductoAdminDetailView.as_view(), name='producto-admin-detail'),
]
