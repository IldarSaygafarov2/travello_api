from django.urls import reverse
from django_filters import rest_framework as filters
from drf_spectacular.utils import extend_schema
from rest_framework import filters as drf_filters
from rest_framework import generics, viewsets
from rest_framework.response import Response

from . import models, serializers


@extend_schema(tags=['Events'])
class EventViewSet(viewsets.ModelViewSet):
    # serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('event_type',)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.EventSimpleSerializer
        return serializers.EventSerializer





