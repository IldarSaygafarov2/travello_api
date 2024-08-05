from rest_framework import generics
from rest_framework.response import Response
from .models import CorporateClientRequest
from .serializers import CorporateClientRequestSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Corporate Clients'])
class CorporateClientRequestView(generics.ListCreateAPIView):
    queryset = CorporateClientRequest.objects.all()
    serializer_class = CorporateClientRequestSerializer