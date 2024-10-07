from rest_framework import generics
from rest_framework.response import Response
from .models import CorporateClientRequest, OurClient
from .serializers import CorporateClientRequestSerializer, OurClientSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Corporate Clients'])
class CorporateClientRequestView(generics.ListCreateAPIView):
    queryset = CorporateClientRequest.objects.all()
    serializer_class = CorporateClientRequestSerializer



@extend_schema(tags=['Corporate Clients'])
class OurClientView(generics.ListAPIView):
    queryset = OurClient.objects.all()
    serializer_class = OurClientSerializer
