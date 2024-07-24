from django.urls import path

from . import views


urlpatterns = [
	path('', views.HotelList.as_view(), name='hotel-list'),
]
