from rest_framework import serializers

from .models import CorporateClientRequest, OurClient


class CorporateClientRequestSerializer(serializers.ModelSerializer):
    khakimiyat_license = serializers.FileField()

    class Meta:
        model = CorporateClientRequest
        fields = [
            "name",
            "email",
            "phone_number",
            "about_company",
            "client_type",
            "khakimiyat_license",
            "uzb_tourism_license",
            "lease_contract",
            "director_passport",
            "charter",
            "address_and_index",
            "fax",
            "corparate_account",
            "mfo",
            "okonx",
            "okpo",
            "created_at",
        ]
        read_only_fields = ["created_at"]


class OurClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurClient
        fields = ["id", "name", "image"]
