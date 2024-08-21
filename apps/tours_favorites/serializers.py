from rest_framework import serializers

from apps.events.serializers import EventSimpleSerializer
from . import models


class TourFavoriteSerializer(serializers.ModelSerializer):
    tour = EventSimpleSerializer(many=False, source='tours')

    class Meta:
        model = models.FavoriteTour
        fields = ['id', 'user', 'tour']
