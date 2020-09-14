from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('manage/', views.manage, name='manage'),
    path('title/', views.add_title, name='add_title'),
    path('sub/', views.add_sub_content, name='add_sub_content'),
]
