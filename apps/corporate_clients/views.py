from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import CorporateClientRequest, OurClient
from .serializers import CorporateClientRequestSerializer, OurClientSerializer


@extend_schema(tags=['Corporate Clients'])
class CorporateClientRequestView(generics.CreateAPIView):
    queryset = CorporateClientRequest.objects.all()
    serializer_class = CorporateClientRequestSerializer


@extend_schema(tags=['Corporate Clients'])
class OurClientView(generics.ListAPIView):
    queryset = OurClient.objects.all()
    serializer_class = OurClientSerializer
