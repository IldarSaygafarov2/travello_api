from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ReviewList.as_view(), name='review-list'),
]