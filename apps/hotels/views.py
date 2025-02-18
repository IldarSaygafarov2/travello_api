import requests
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import filters, generics
from rest_framework.response import Response

from travello import settings
from . import models, serializers
from ..users.models import User


@extend_schema(tags=["Hotels"])
class HotelListView(generics.ListAPIView):
    queryset = models.Hotel.objects.all()

    serializer_class = serializers.HotelListSerializer
    filter_backends = (
        filters.OrderingFilter,
        DjangoFilterBackend,
    )
    filterset_fields = ("hotel_type",)


@extend_schema(tags=["Hotels"])
class HotelDetailView(generics.RetrieveAPIView):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelDetailSerializer
    lookup_url_kwarg = "hotel_id"


@extend_schema(tags=["Hotels"])
class HotelRoomsListView(generics.ListAPIView):
    queryset = models.HotelRoom.objects.all()
    serializer_class = serializers.HotelRoomSerializer
    lookup_url_kwarg = "hotel_id"

    def get_queryset(self):
        hotel_id = self.kwargs.get("hotel_id")
        return models.HotelRoom.objects.filter(hotel_id=hotel_id)


@extend_schema(tags=["Hotels"])
class HotelRoomDetailView(generics.RetrieveAPIView):
    queryset = models.HotelRoom.objects.all()
    serializer_class = serializers.HotelRoomSerializer
    lookup_url_kwarg = "room_id"

    def retrieve(self, request, *args, **kwargs):
        hotel_id = kwargs.get("hotel_id")
        room_id = kwargs.get("room_id")

        hotel_rooms = models.HotelRoom.objects.filter(hotel_id=hotel_id)
        if not hotel_rooms:
            return Response([])

        room = hotel_rooms.filter(pk=room_id)
        if not room:
            return Response([])

        room_serializer = self.serializer_class(room.first(), many=False)
        return Response(room_serializer.data, status=200)


@extend_schema(tags=["Hotels"])
class HotelBookingView(generics.ListCreateAPIView):
    queryset = models.HotelBooking.objects.all()
    serializer_class = serializers.HotelBookingSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)

        print(data.data)
        user = User.objects.get(pk=data.data['user'])
        hotel = models.Hotel.objects.get(pk=data.data['hotel'])
        hotel_room = models.HotelRoom.objects.get(pk=data.data['hotel_room'])
        msg = f'''
Бронь отеля

Пользователь: {user.first_name} {user.last_name}
Отель: {hotel.name}
Комната в отеле: {hotel_room.name}
Кол-во отдыхающих: {data.data['tourists_quantity']}
Кол-во детей: {data.data['children_quantity']}
        '''
        requests.post(
            url=settings.TG_API_URL.format(
                token=settings.MAIN_BOT_TOKEN,
                channel_id=settings.TOUR_BOOKINGS_CHANNEL,
                text=msg,
            )
        )

        return data
