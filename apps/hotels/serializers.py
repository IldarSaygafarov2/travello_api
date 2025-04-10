from rest_framework import serializers
from . import models


# hotel room serializers start


class HotelRoomImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelRoomImages
        fields = ["id", "image"]


class HotelRoomFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelRoomFacilities
        fields = ["id", "facility"]


class HotelSeasonPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelPriceInSeason
        fields = ["pk", "start", "end", "price_for_resident", "price_for_not_resident"]


class HotelNotSeasonPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelPriceInSeason
        fields = ["pk", "start", "end", "price_for_resident", "price_for_not_resident"]


class HotelRoomSerializer(serializers.ModelSerializer):
    room_images = HotelRoomImagesSerializer(many=True)
    room_facilities = HotelRoomFacilitiesSerializer(many=True)
    price_in_season = HotelSeasonPriceSerializer(many=True)
    price_in_not_season = HotelNotSeasonPriceSerializer(many=True)

    class Meta:
        model = models.HotelRoom
        fields = [
            "id",
            "name",
            "description",
            "price",
            "hotel",
            "room_images",
            "room_facilities",
            "price_in_season",
            "price_in_not_season",
            "is_all_inclusive",
        ]


# hotel room serializers end


# hotel serializers start


class HotelGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelGallery
        fields = ["id", "photo"]


class HotelListSerializer(serializers.ModelSerializer):
    reviews_quantity = serializers.SerializerMethodField(
        method_name="get_reviews_quantity"
    )
    rating = serializers.SerializerMethodField(method_name="get_rating")

    class Meta:
        model = models.Hotel
        fields = [
            "id",
            "name",
            "preview",
            "city",
            "country",
            "rating",
            "reviews_quantity",
            "minimum_price",
            "hotel_type",
            "is_all_inclusive",
            "fee",
            "stars",
        ]

    @staticmethod
    def get_reviews_quantity(obj) -> int:
        return obj.reviews.count()

    @staticmethod
    def get_rating(obj) -> int:
        return obj.get_rating_display()


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_gallery = HotelGallerySerializer(many=True, read_only=True)
    rooms = HotelRoomSerializer(many=True, read_only=True)

    allocation_type = serializers.SerializerMethodField(
        method_name="get_allocation_type"
    )

    class Meta:
        model = models.Hotel
        fields = [
            "id",
            "name",
            "preview",
            "minimum_price",
            "country",
            "address",
            "full_description",
            "allocation_type",
            "stars",
            "nights",
            "total_people",
            "hotel_gallery",
            "rooms",
            "is_all_inclusive",
            "price_for_child",
            "fee",
            "map_code"
        ]

    @staticmethod
    def get_allocation_type(obj) -> str:
        return obj.get_allocation_type_display()


class HotelBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelBooking
        fields = [
            "user",
            "hotel",
            "hotel_room",
            "tourists_quantity",
            "children_quantity",
        ]


# hotel serializers end
