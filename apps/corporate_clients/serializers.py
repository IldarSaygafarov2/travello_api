from rest_framework.serializers import ModelSerializer

from .models import CorporateClientRequest


class CorporateClientRequestSerializer(ModelSerializer):
    class Meta:
        model = CorporateClientRequest
        fields = '__all__'
        