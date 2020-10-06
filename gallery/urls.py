from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_gallery, name='gallery'),
    path('<int:img_id>/', views.image_detail, name='image_detail'),
    path('add/', views.add_image, name='add_image'),
    path('edit/<int:img_id>/', views.edit_image, name='edit_image'),
    path('delete/<int:img_id>/', views.delete_image, name='delete_image'),
]
