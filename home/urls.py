from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('manage/', views.manage, name='manage'),
    path('contact/', views.contact, name='contact'),
    path('title/<int:title_id>/', views.title_detail, name='title_detail'),
    path('slide/<int:slides_id>/', views.slides_detail, name='slides_detail'),
    path('slides/add', views.add_slides, name='add_slides'),
    path('slide/edit/<int:slides_id>/', views.edit_slides, name='edit_slides'),
    path('title/edit/<int:title_id>/', views.edit_title, name='edit_title'),
    path(
        'slides/delete/<int:slides_id>/',
        views.delete_slides, name='delete_slides'),
]
