from rest_framework import serializers

from apps.users.serializers import UserInfoSerializer, PassportSerializer

from . import models
from .models import Guide


class GuideLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GuideLanguage
        fields = ['pk', 'lang']


class GuidePassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GuidePassport
        fields = ['id', 'seria_and_number', 'issued_date', 'issued_by',
                  'citizen', 'agree_to_save_data', 'ready_for_trip']


class GuideSerializer(serializers.ModelSerializer):
    languages = GuideLanguageSerializer(many=True, required=False, read_only=True)
    info = UserInfoSerializer(many=False, source='user', required=False, read_only=True)
    passport_data = GuidePassportSerializer(many=False, required=False, source='passports', read_only=True)

    class Meta:
        model = models.Guide
        fields = ['pk', 'info', 'passport_data', 'about_me', 'avatar', 'languages']


class GuideProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField(method_name='get_first_name')

    class Meta:
        model = models.Guide
        fields = ['pk', 'first_name', 'experience', 'avatar']

    @staticmethod
    def get_first_name(obj: Guide) -> str:
        return obj.user.first_name




class GuideTourExpectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GuideTourExpectation
        fields = ['id', 'guide_tour', 'text']


class GuideTourOrganizationalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GuideTourOrganizationalDetail
        fields = ['id', 'guide_tour', 'text']


class GuideScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GuideSchedule
        fields = ['id', 'guide_tour', 'date', 'time']


class GuideTourPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GuideTourPhoto
        fields = ['id', 'image']


class GuideTourSerializer(serializers.ModelSerializer):
    expectations = GuideTourExpectationSerializer(many=True)
    organizational_details = GuideTourOrganizationalDetailSerializer(many=True)
    schedules = GuideScheduleSerializer(many=True)
    photos = GuideTourPhotoSerializer(many=True)
    # language = serializers.SerializerMethodField(method_name='get_language')
    # tour_duration = serializers.SerializerMethodField(method_name='get_tour_duration')
    # number_of_people = serializers.SerializerMethodField(method_name='get_number_of_people')
    # mode_of_transportation = serializers.SerializerMethodField(method_name='get_mode_of_transportation')
    # working_with_orders = serializers.SerializerMethodField(method_name='get_working_with_orders')

    class Meta:
        model = models.GuideTour
        fields = [
            'id',
            'title',
            'description',
            'additional',
            'city',
            'gathering_place',
            'language',
            # 'tour_duration',
            # 'number_of_people',
            # 'mode_of_transportation',
            # 'working_with_orders',
            'price',
            'expectations',
            'organizational_details',
            'schedules',
            'photos',
        ]

    # @staticmethod
    # def get_language(obj: models.GuideTour) -> str:
    #     return obj.get_language_display()
    #
    # @staticmethod
    # def get_tour_duration(obj: models.GuideTour) -> str:
    #     return obj.get_tour_duration_display()
    #
    # @staticmethod
    # def get_number_of_people(obj: models.GuideTour) -> str:
    #     return obj.get_number_of_people_display()
    #
    # @staticmethod
    # def get_mode_of_transportation(obj: models.GuideTour) -> str:
    #     return obj.get_mode_of_transportation_display()
    #
    # @staticmethod
    # def get_working_with_orders(obj: models.GuideTour) -> str:
    #     return obj.get_working_with_orders_display()


class GuideTourCreateSerializer(serializers.ModelSerializer):
    expectations = GuideTourExpectationSerializer(many=True, required=False)
    organizational_details = GuideTourOrganizationalDetailSerializer(many=True, required=False)
    schedules = GuideScheduleSerializer(many=True, required=False)
    photos = GuideTourPhotoSerializer(many=True, required=False)

    class Meta:
        model = models.GuideTour
        fields = [
            'id',
            'guide',
            'title',
            'description',
            'additional',
            'city',
            'gathering_place',
            'language',
            'duration',
            'participants_number',
            'transportation_type',
            'price',
            'expectations',
            'organizational_details',
            'schedules',
            'photos',
        ]
