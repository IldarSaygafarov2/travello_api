from django.urls import path

from . import views

urlpatterns = [
    path('', views.EventSimpleView.as_view(), name='events'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('<int:pk>/book/', views.EventBookingView.as_view(), name='event-booking'),

]
