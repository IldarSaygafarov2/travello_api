from django.shortcuts import render
from rest_framework.response import Response
from . import serializers
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from . import models


@extend_schema(tags=['Events'])
class EventListView(generics.ListAPIView):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()


@extend_schema(tags=['Events'])
class EventDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    lookup_field = 'slug'