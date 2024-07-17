from drf_spectacular.utils import extend_schema
from rest_framework import generics

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
