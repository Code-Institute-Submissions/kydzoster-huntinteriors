from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('manage/', views.manage, name='manage'),
    path('slides/', views.slides, name='slides'),
    path('title/', views.add_title, name='add_title'),
    path('<int:main_id>/', views.title_detail, name='title_detail'),
    path('sub/', views.add_sub_content, name='add_sub_content'),
    path('<int:sub_id>/', views.sub_detail, name='sub_detail'),
]
