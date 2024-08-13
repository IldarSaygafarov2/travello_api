from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
from . import models, serializers


@extend_schema(tags=['Hotels'])
class HotelList(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelDetailSerializer
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = serializers.HotelListSerializer(qs, many=True)
        return Response(serializer.data)