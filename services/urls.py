from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('edit/<int:serv_id>/', views.edit_services, name='edit_services'),
    path('<int:serv_id>/', views.services_detail, name='services_detail'),
    path('add', views.add_services, name='add_services'),
    path(
        'delete/<int:serv_id>/',
        views.delete_services, name='delete_services'),
]
