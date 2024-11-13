from django.urls import path
from . import views



urlpatterns = [
    path('', views.OurClientView.as_view(), name='our-clients'),
    path('corporate/', views.CorporateClientRequestView.as_view(), name='corporate-client-request'),
]
