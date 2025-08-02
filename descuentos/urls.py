# descuentos/urls.py
from django.urls import path
from .views import DescuentoPublicView, DescuentoAdminView, DescuentoAdminDetailView

urlpatterns = [
    # Vista pública: solo GET
    path('public/desc/', DescuentoPublicView.as_view(), name='descuento-public-list'),
    
    # Vista de admin: GET, POST, PATCH, DELETE
    path('desc/', DescuentoAdminView.as_view(), name='descuentos-admin'),
    path('desc/<int:pk>/', DescuentoAdminDetailView.as_view(), name='descuento-detail'),
]
