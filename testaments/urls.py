from django.urls import path
from .views import *

urlpatterns = [
    path(
        '<int:pk>/edit/',
        TestamentUpdateView.as_view(),
        name='testament_edit'),
    path(
        '<int:pk>/',
        TestamentDetailView.as_view(),
        name='testament_detail'),
    path(
        '<int:pk>/delete/',
        TestamentDeleteView.as_view(),
        name='testament_delete'),
    path('add/', TestamentCreateView.as_view(), name='testament_add'),
    path('review_list/', TestamentReviewList.as_view(), name='testament_review_list'),
    path('approve/<int:pk>/', TestamentApproveView.as_view(), name='testament_approve'),
    path('', TestamentListView.as_view(), name='testament_list'),
]
