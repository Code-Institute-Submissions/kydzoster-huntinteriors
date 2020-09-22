from django.urls import path
from .views import TestamentListView, TestamentDetailView,\
    TestamentCreateView, TestamentUpdateView, TestamentDeleteView


urlpatterns = [
    path(
        'post/<int:pk>/delete/',
        TestamentDeleteView.as_view(), name='post_delete'),
    path(
        'post/<int:pk>/edit/',
        TestamentUpdateView.as_view(), name='post_edit'),
    path('post/new/', TestamentCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', TestamentDetailView.as_view(), name='post_detail'),
    path('', TestamentListView.as_view(), name='testament'),
]
