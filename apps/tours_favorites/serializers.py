from rest_framework import serializers

from apps.events.serializers import EventSimpleSerializer
from apps.events.models import Event
from . import models


class TourFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteTour
        fields = ['id', 'user', 'tours']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        tour = Event.objects.get(id=instance.tours.id)
        tour_serializer = EventSimpleSerializer(tour)
        data['tours'] = tour_serializer.data
        return data
