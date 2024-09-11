from rest_framework import serializers
from .models import Newsletter, StaticMediaContent, StaticMediaContentItem


class NewsletterSerializer(serializers.ModelSerializer):
    is_answered = serializers.BooleanField(required=False)

    class Meta:
        model = Newsletter
        fields = ['id', 'name', 'email', 'text', 'is_answered']


class StaticMediaContentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticMediaContentItem
        fields = ['pk', 'media']


class StaticMediaContentSerializer(serializers.ModelSerializer):
    content = StaticMediaContentItemSerializer(many=True, source='media_content', read_only=True)
    class Meta:
        model = StaticMediaContent
        fields = ['pk', 'page', 'page_slug', 'content']