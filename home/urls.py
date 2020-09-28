from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('manage/', views.manage, name='manage'),
    path('<int:sub_id>/', views.sub_detail, name='sub_detail'),
    path('add/', views.add_content, name='add_content'),
    path('edit/<int:sub_id>/', views.edit_content, name='edit_content'),
    path('delete/<int:sub_id>/', views.delete_content, name='delete_content'),
    path('contact/', views.contact, name='contact'),
]
