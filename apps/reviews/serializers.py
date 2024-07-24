from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(source='get_user_type_display')

    class Meta:
        model = Review
        fields = ['id', 'fullname', 'avatar', 'text', 'user_type']