from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics

from . import models, serializers
from .filters import EventSearchFilter


@extend_schema(tags=['Events'])
class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('event_type',)
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.EventSimpleSerializer
        return serializers.EventSerializer


@extend_schema(tags=['Events'])
class TopEventsListView(generics.ListAPIView):
    serializer_class = serializers.EventSimpleSerializer

    def get_queryset(self):
        return models.Event.objects.filter(is_event_top=True)[:4]


@extend_schema(tags=['Events'])
class EventSearchView(generics.ListAPIView):
    serializer_class = serializers.EventSimpleSerializer
    queryset = models.Event.objects.all()
    # filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventSearchFilter


