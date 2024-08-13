from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema
from rest_framework import filters as drf_filters
from rest_framework import generics
from django.urls import reverse_lazy, reverse
from . import models, serializers
from rest_framework.response import Response

@extend_schema(tags=['Events'])
class EventListView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    filter_backends = (drf_filters.SearchFilter, filters.DjangoFilterBackend, )
    search_fields = ('title', )
    filterset_fields = ('event_type',)


@extend_schema(tags=['Events'])
class EventDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()


@extend_schema(tags=['Events'])
class EventSimpleView(generics.ListAPIView):
    serializer_class = serializers.EventSimpleSerializer
    queryset = models.Event.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('event_type',)
    

@extend_schema(tags=['Events'])
class EventBookingView(generics.ListCreateAPIView):
    serializer_class = serializers.EventBookingSerializer
    queryset = models.EventBooking.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer_data = serializer.data
        serializer_data['add_children_url'] = reverse('users:children-list', kwargs={'user_pk': data['user']})
        serializer_data['add_tourist_url'] = reverse('users:tourist-list', kwargs={'user_pk': data['user']})
        return Response(serializer_data)



