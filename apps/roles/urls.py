from django.urls import path

from . import views


urlpatterns = [
    path('guides/<int:pk>/', views.GuideDetailView.as_view())
]