from django.urls import path
from rest_framework import routers
from apps.tours_booked.urls import urlpatterns as tours_booked_urlpatterns
from . import views


router = routers.DefaultRouter()
router.register(r'', views.EventViewSet)


urlpatterns = [
    path('popular/', views.TopEventsListView.as_view()),
    path('search/', views.EventSearchView.as_view())
]

urlpatterns += router.urls + tours_booked_urlpatterns
