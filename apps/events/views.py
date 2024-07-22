from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework import filters as drf_filters

from . import models, serializers
from django_filters import rest_framework as filters


@extend_schema(tags=['Events'])
class EventListView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
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
    

# @extend_schema(tags=['Events'])
# class EventSearchView(generics.ListAPIView):
#     queryset = models.Event.objects.all()
#     filter_backends = [drf_filters.SearchFilter]
#     search_fields = ['country_from', 'country', 'event_start', 'people_in_group']
    