from django.urls import path
from . import views


urlpatterns = [
    path('<int:event_id>/book/', views.EventBookingView.as_view(), name='event-booking'),
]
