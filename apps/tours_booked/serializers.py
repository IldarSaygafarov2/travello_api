from rest_framework import serializers
from apps.users.serializers import TouristSerializer
from . import models


class EventBookingSerializer(serializers.ModelSerializer):
    tourists = TouristSerializer(many=True)

    class Meta:
        model = models.EventBooking
        fields = [
            "id",
            "user",
            "event",
            "tourists",
            "total_adult",
            "total_children",
            "event_type",
        ]
