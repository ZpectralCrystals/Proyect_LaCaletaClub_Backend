# blogs/urls.py
from django.urls import path
from .views import BlogPublicView, BlogAdminView, BlogAdminDetailView

urlpatterns = [
    # Vista pública: solo GET
    path('public/blogs/', BlogPublicView.as_view(), name='blog-public-list'),
    
    # Vista de admin: GET, POST, PATCH, DELETE
    path('blogs/', BlogAdminView.as_view(), name='blog-admin-list'),
    path('blogs/<int:pk>/', BlogAdminDetailView.as_view(), name='blog-admin-detail'),
]
