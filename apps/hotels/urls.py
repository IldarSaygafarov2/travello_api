from django.urls import path

from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register(r'', views.HotelList)

urlpatterns = [

]

urlpatterns += router.urls
