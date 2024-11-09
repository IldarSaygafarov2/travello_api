from rest_framework import serializers
from . import models


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
    rating = serializers.SerializerMethodField(method_name='get_rating')

    class Meta:
        model = models.Hotel
        fields = ['id', 'name', 'preview', 'city', 'country', 'rating', 'reviews_quantity']

    @staticmethod
    def get_reviews_quantity(obj) -> int:
        return obj.reviews.count()

    @staticmethod
    def get_rating(obj) -> int:
        return obj.get_rating_display()


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_gallery = HotelGallerySerializer(many=True, read_only=True)
    hotel_facilities = HotelFacilitiesSerializer(many=True, read_only=True, source='facilities')
    hotel_entertainment = HotelEntertainmentSerializer(many=True, read_only=True, source='entertainment')
    rooms = HotelRoomSerializer(many=True, read_only=True)

    allocation_type = serializers.SerializerMethodField(method_name='get_allocation_type')

    class Meta:
        model = models.Hotel
        fields = [
            'id',
            'name',
            'country',
            'address',
            'full_description',
            'allocation_type',
            'stars',
            'nights',
            'total_people',
            'event',
            'hotel_gallery',
            'hotel_facilities',
            'hotel_entertainment',
            'rooms'
        ]

    @staticmethod
    def get_allocation_type(obj) -> str:
        return obj.get_allocation_type_display()

# hotel serializers end
