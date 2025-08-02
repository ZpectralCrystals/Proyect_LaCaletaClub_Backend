# recomendaciones/urls.py
from django.urls import path
from .views import RecomendacionesPublicView, RecomendacionesAdminView, RecomendacionesAdminDetailView

urlpatterns = [
    # Vista pública: solo GET
    path('public/recomendaciones/', RecomendacionesPublicView.as_view(), name='recomendaciones-public-list'),
    
    # Vista de admin: GET, POST, PATCH, DELETE
    path('recomendaciones/', RecomendacionesAdminView.as_view(), name='recomendaciones-admin-list'),
    path('recomendaciones/<int:pk>/', RecomendacionesAdminDetailView.as_view(), name='recomendaciones-admin-detail'),
]
