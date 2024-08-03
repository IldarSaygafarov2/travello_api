from django.urls import path

from . import views

urlpatterns = [
    path('', views.EventSimpleView.as_view(), name='events'),
    path('<slug:slug>/', views.EventDetailView.as_view(), name='event-detail'),
]
