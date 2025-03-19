from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(source="get_user_type_display")

    class Meta:
        model = Review
        fields = [
            "id",
            "fullname",
            "avatar",
            "text",
            "user_type",
            "review_type",
            "event",
            "hotel",
        ]


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["hotel", "review_type", "text", "fullname", "user_type", "photo"]
