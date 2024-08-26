from django.urls import reverse
from drf_spectacular.utils import extend_schema
from rest_framework import generics, viewsets
from rest_framework.response import Response

from . import serializers, models


@extend_schema(tags=['Events Booking'])
class EventBookingView(generics.ListCreateAPIView):
    serializer_class = serializers.EventBookingSerializer
    queryset = models.EventBooking.objects.all()
    lookup_url_kwarg = 'event_id'

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer_data = serializer.data
        serializer_data['add_children_url'] = reverse('users:children-list', kwargs={'user_pk': data['user']})
        serializer_data['add_tourist_url'] = reverse('users:tourist-list', kwargs={'user_pk': data['user']})
        return Response(serializer_data)


@extend_schema(tags=['User Events Booking'])
class EventBookingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventBookingSerializer
    queryset = models.EventBooking.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user_id=self.kwargs['user_pk'])
