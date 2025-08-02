# anuncios/urls.py
from django.urls import path
from .views import AnuncioPublicView, AnuncioAdminView, AnuncioAdminDetailView

urlpatterns = [
    # Vista pública: solo GET
    path('public/anuncios/', AnuncioPublicView.as_view(), name='anuncio-public-list'),
    
    # Vista de admin: GET, POST, PATCH, DELETE
    path('anuncios/', AnuncioAdminView.as_view(), name='anuncio-admin-list'),
    path('anuncios/<int:pk>/', AnuncioAdminDetailView.as_view(), name='anuncio-admin-detail'),
]
