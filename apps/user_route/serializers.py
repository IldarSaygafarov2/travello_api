from rest_framework import serializers


from apps.users.serializers import TouristSerializer


from .models import (
    UserTourRoute,
    UserTourHotel,
    UserTourTransport
)


class UserRouteSerializer(serializers.ModelSerializer):
    tourists = serializers.SerializerMethodField(method_name='get_tourists')
    hotels = serializers.SerializerMethodField(method_name='get_hotels')
    transports = serializers.SerializerMethodField(method_name='get_transports')
    guide = serializers.SerializerMethodField(method_name='get_guide')
    insurance = serializers.SerializerMethodField(method_name='get_insurance')
    additional_services = serializers.SerializerMethodField(method_name='get_additional_services')

    class Meta:
        model = UserTourRoute
        fields = [
            'id',
            'tourists',
            'hotels',
            'transports',
            'guide',
            'insurance',
            'additional_services'
        ]

    @staticmethod
    def get_tourists(obj):
        return []

    @staticmethod
    def get_hotels(obj):
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


class UserRouteCreateSerializer(serializers.ModelSerializer):
    tourists = TouristSerializer(many=True, source='user.tourists', required=False)
    hotels = UserTourHotelSerializer(many=True, required=False)
    transports = UserTourTransportSerializer(many=True, required=False)

    class Meta:
        model = UserTourRoute
        fields = ['user', 'tourists', 'hotels', 'transports']