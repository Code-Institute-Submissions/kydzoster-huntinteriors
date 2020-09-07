from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<gallery_id>', views.gallery_detail, name='gallery_detail'),
]
