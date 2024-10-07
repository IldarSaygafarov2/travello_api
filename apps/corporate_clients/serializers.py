from rest_framework.serializers import ModelSerializer

from .models import CorporateClientRequest, OurClient


class CorporateClientRequestSerializer(ModelSerializer):
    class Meta:
        model = CorporateClientRequest
        fields = '__all__'



class OurClientSerializer(ModelSerializer):
    class Meta:
        model = OurClient
        fields = ['id', 'name', 'image']