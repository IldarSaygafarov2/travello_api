from django.urls import path

from . import views

urlpatterns = [
    path('', views.HotelListView.as_view()),
    path('<int:hotel_id>/', views.HotelDetailView.as_view()),
    path('<int:hotel_id>/rooms/', views.HotelRoomsListView.as_view()),
    path('<int:hotel_id>/rooms/<int:room_id>/', views.HotelRoomDetailView.as_view())
]

