from rest_framework import serializers
from apps.users.serializers import TouristSerializer, ChildrenSerializer
from . import models
from ..users.models import Tourist


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


class EventSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ['id', 'title', 'preview', 'slug', 'days', 'price', 'event_start', 'event_end']
        
        
class EventSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ['country_from', 'country', 'event_start', 'nights', 'people_in_group']


class TourBookingSerializer(serializers.ModelSerializer):
    tourists = TouristSerializer(many=True)

    class Meta:
        model = models.TourBooking
        fields = [
            'id',
            'number_of_people',
            'number_of_children',
            'tourists',
            'event'
        ]

    def create(self, validated_data):
        tourists = validated_data.pop('tourists')
        tour_book = models.TourBooking(**validated_data)
        tour_book.save()
        for tourist in tourists:
            # create tourist object
            tourist_obj = Tourist.objects.create(**tourist)
            tourist_obj.save()
            tour_book.tourists.add(tourist_obj)
        return tour_book
        # tourists_serializer = TouristSerializer(tourists, many=True)
        # validated_data['tourists'] = tourists_serializer.data
        # return models.TourBooking.objects.create(**validated_data)