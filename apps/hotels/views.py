from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import filters, viewsets
from .filters import HotelAirPortDistanceFilter
from . import models, serializers


@extend_schema(tags=['Hotels'])
class HotelList(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelDetailSerializer
    http_method_names = ['get']
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend,)
    filterset_class = HotelAirPortDistanceFilter
    ordering_fields = ['price',]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.HotelListSerializer
        return serializers.HotelDetailSerializer
