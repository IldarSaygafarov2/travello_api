from django.db.models import Count
from rest_framework import serializers
from . import models
from apps.events.serializers import EventSerializer


# hotel room serializers start


class HotelRoomImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelRoomImages
        fields = [
            'id',
            'image'
        ]


class HotelRoomFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelRoomFacilities
        fields = [
            'id',
            'facility'
        ]


class HotelRoomSerializer(serializers.ModelSerializer):
    room_images = HotelRoomImagesSerializer(many=True)
    room_facilities = HotelRoomFacilitiesSerializer(many=True)

    class Meta:
        model = models.HotelRoom
        fields = [
            'id',
            'name',
            'is_all_inclusive',
            'description',
            'nights',
            'price',
            'until',
            'hotel',
            'room_images',
            'room_facilities',
        ]


# hotel room serializers end


# hotel serializers start
class HotelEntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelEntertainment
        fields = ['id', 'name']


class HotelGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelGallery
        fields = ['id', 'photo']


class HotelFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelFacility
        fields = ['id', 'name']


class HotelListSerializer(serializers.ModelSerializer):
    reviews_quantity = serializers.SerializerMethodField(method_name='get_reviews_quantity')

    class Meta:
        model = models.Hotel
        fields = ['id', 'name', 'price', 'preview', 'city', 'country', 'rating', 'reviews_quantity']


    def get_reviews_quantity(self, obj):
        return obj.reviews.count()


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_gallery = HotelGallerySerializer(many=True, read_only=True)
    hotel_facilities = HotelFacilitiesSerializer(many=True, read_only=True, source='facilities')
    hotel_entertainment = HotelEntertainmentSerializer(many=True, read_only=True, source='entertainment')
    rooms = HotelRoomSerializer(many=True, read_only=True)

    beach_line = serializers.SerializerMethodField(method_name='get_beach_line')
    coordinates = serializers.SerializerMethodField(method_name='get_coordinates')
    beach_type = serializers.SerializerMethodField(method_name='get_beach_type')
    allocation_type = serializers.SerializerMethodField(method_name='get_allocation_type')

    class Meta:
        model = models.Hotel
        fields = [
            'id',
            'name',
            'country',
            'address',
            'short_description',
            'full_description',
            'is_meals_included',
            'allocation_type',
            'stars',
            'price',
            'distance_to_beach',
            'distance_to_airport',
            'coordinates',
            'nights',
            'total_people',
            'has_wifi',
            'beach_line',
            'beach_type',
            'event',
            'hotel_gallery',
            'hotel_facilities',
            'hotel_entertainment',
            'rooms'
        ]

    def get_beach_line(self, obj) -> str:
        return obj.get_beach_line_display()

    def get_beach_type(self, obj) -> str:
        return obj.get_beach_type_display()

    def get_coordinates(self, obj) -> str:
        return f'{obj.latitude}, {obj.longitude}'

    def get_allocation_type(self, obj) -> str:
        return obj.get_allocation_type_display()

# hotel serializers end
