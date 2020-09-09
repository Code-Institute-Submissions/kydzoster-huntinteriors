from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<int:gallery_id>/', views.gallery_detail, name='gallery_detail'),
    path('add/', views.add_gallery, name='add_gallery'),
]
