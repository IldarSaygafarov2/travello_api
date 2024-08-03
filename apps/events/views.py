from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema
from rest_framework import filters as drf_filters
from rest_framework import generics

from . import models, serializers


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
    lookup_field = 'slug'


@extend_schema(tags=['Events'])
class EventSimpleView(generics.ListAPIView):
    serializer_class = serializers.EventSimpleSerializer
    queryset = models.Event.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('event_type',)
    

