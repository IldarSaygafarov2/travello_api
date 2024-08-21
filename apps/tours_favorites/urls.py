from django.urls import path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'favorite_tours', views.FavoriteTourView)


urlpatterns = [

]
