from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/send/', views.NewsletterView.as_view())
]
