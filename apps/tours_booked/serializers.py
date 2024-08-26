from rest_framework import serializers
from . import models


class EventBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EventBooking
        fields = ['id', 'user', 'event', 'total_adult', 'total_children', 'event_type']
