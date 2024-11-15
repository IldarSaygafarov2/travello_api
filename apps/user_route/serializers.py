from rest_framework import serializers


from apps.users.serializers import TouristSerializer
from apps.users.models import Tourist

from .models import (
    UserTourRoute,
    UserTourHotel,
    UserTourTransport,
    UserRouteGuide,
    UserRouteAdditionalService
)
from ..hotels.models import Hotel


class UserTourHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTourHotel
        fields = [
            'user_route',
            'hotel',
            'room'
        ]


class UserTourTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTourTransport
        fields = [
            'user_route',
            'transport_type',
            'transfer_type',
            'from_to',
            'hotel_details',
            'number_of_tourists',
        ]


class UserRouteGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRouteGuide
        fields = ['user_route', 'guide']


class UserRouteAdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRouteAdditionalService
        fields = ['user_route', 'photo_video_shooting', 'open_sim_card']


class UserRouteSerializer(serializers.ModelSerializer):
    tourists = serializers.SerializerMethodField(method_name='get_tourists')
    hotels = serializers.SerializerMethodField(method_name='get_hotels')
    # transports = UserTourTransportSerializer(many=True)
    # guide = UserRouteGuideSerializer(many=True)
    # additional_services = UserRouteAdditionalServiceSerializer(many=True)
    #
    # insurance = serializers.SerializerMethodField(method_name='get_insurance')

    class Meta:
        model = UserTourRoute
        fields = [
            'id',
            'tourists',
            'hotels',
            # 'transports',
            # 'guide',
            # 'insurance',
            # 'additional_services'
        ]

    @staticmethod
    def get_tourists(obj:  UserTourRoute):
        tourists = Tourist.objects.filter(user=obj.user)
        tourists_serializer = TouristSerializer(tourists, many=True)
        return tourists_serializer.data

    @staticmethod
    def get_hotels(obj: UserTourRoute):
        user_route_hotel = UserTourHotel.objects.filter(user_route=obj)
        print(user_route_hotel)
        return []

    @staticmethod
    def get_transports(obj):
        return []

    @staticmethod
    def get_guide(obj):
        return []

    @staticmethod
    def get_insurance(obj):
        return []

    @staticmethod
    def get_additional_services(obj):
        return []


class UserRouteCreateSerializer(serializers.ModelSerializer):
    tourists = TouristSerializer(many=True, source='user.tourists', required=False)
    hotels = UserTourHotelSerializer(many=True, required=False)
    transports = UserTourTransportSerializer(many=True, required=False)
    guides = UserRouteGuideSerializer(many=True, required=False)
    additional_services = UserRouteAdditionalServiceSerializer(many=True, required=False)

    class Meta:
        model = UserTourRoute
        fields = ['id', 'user', 'tourists', 'hotels', 'transports', 'guides', 'additional_services']