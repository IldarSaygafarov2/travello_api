from django.urls import path
from . import views



urlpatterns = [
    path('corporate/', views.CorporateClientRequestView.as_view(), name='corporate-client-request'),
    path('list/', views.OurClientView.as_view(), name='our-clients'),
]