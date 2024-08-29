from django.urls import path
from rest_framework import routers
from apps.tours_booked.urls import urlpatterns as tours_booked_urlpatterns
from . import views


router = routers.DefaultRouter()
router.register(r'', views.EventViewSet)


urlpatterns = []

urlpatterns += router.urls + tours_booked_urlpatterns
