from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import filters, generics
from rest_framework.response import Response

from . import models, serializers


@extend_schema(tags=['Hotels'])
class HotelListView(generics.ListAPIView):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelListSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend,)


@extend_schema(tags=['Hotels'])
class HotelDetailView(generics.RetrieveAPIView):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelDetailSerializer
    lookup_url_kwarg = 'hotel_id'


@extend_schema(tags=['Hotels'])
class HotelRoomsListView(generics.ListAPIView):
    queryset = models.HotelRoom.objects.all()
    serializer_class = serializers.HotelRoomSerializer
    lookup_url_kwarg = 'hotel_id'

    def get_queryset(self):
        hotel_id = self.kwargs.get('hotel_id')
        return models.HotelRoom.objects.filter(hotel_id=hotel_id)


@extend_schema(tags=['Hotels'])
class HotelRoomDetailView(generics.RetrieveAPIView):
    queryset = models.HotelRoom.objects.all()
    serializer_class = serializers.HotelRoomSerializer
    lookup_url_kwarg = 'room_id'

    def retrieve(self, request, *args, **kwargs):
        hotel_id = kwargs.get('hotel_id')
        room_id = kwargs.get('room_id')

        hotel_rooms = models.HotelRoom.objects.filter(hotel_id=hotel_id)
        if not hotel_rooms:
            return Response([])

        room = hotel_rooms.filter(pk=room_id)
        if not room:
            return Response([])

        room_serializer = self.serializer_class(room.first(), many=False)
        return Response(room_serializer.data, status=200)
