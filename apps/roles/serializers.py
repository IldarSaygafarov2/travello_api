from rest_framework import serializers

from .models import Guide, GuideLanguage
from apps.users.serializers import UserInfoSerializer


class GuideLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideLanguage
        fields = ['pk', 'lang']


class GuideSerializer(serializers.ModelSerializer):
    languages = GuideLanguageSerializer(many=True)
    info = UserInfoSerializer(many=False, source='user')

    class Meta:
        model = Guide
        fields = ['pk', 'info', 'about_me', 'languages']
