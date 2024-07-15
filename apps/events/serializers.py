from rest_framework import serializers
from . import models


class EventGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventGallery
        fields = ['id', 'image']


class EventTourProgramGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventTourProgramGallery
        fields = ['id', 'image']


class EventTourProgramSerializer(serializers.ModelSerializer):
    tour_program_gallery = EventTourProgramGallerySerializer(many=True)

    class Meta:
        model = models.EventTourProgram
        fields = ['id', 'title', 'day', 'description', 'tour_program_gallery']


class EventPriceIncludedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventPriceIncluded
        fields = ['id', 'title']


class EventPriceNotIncludedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventPriceNotIncluded
        fields = ['id', 'title']


class EventSerializer(serializers.ModelSerializer):
    gallery = EventGallerySerializer(many=True, source='images_gallery')
    tour_program = EventTourProgramSerializer(many=True)
    price_included = EventPriceIncludedSerializer(many=True)
    price_not_included = EventPriceNotIncludedSerializer(many=True)

    class Meta:
        model = models.Event
        fields = [
            'id',
            'title',
            'short_description',
            'full_description',
            'slug',
            'preview',
            'price',
            'country',
            'event_start',
            'event_end',
            'days',
            'nights',
            'gathering_place',
            'minimum_age',
            'people_in_group',
            'event_type',
            'gallery',
            'tour_program',
            'price_included',
            'price_not_included',
        ]
