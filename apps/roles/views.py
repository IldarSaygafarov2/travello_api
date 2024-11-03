from drf_spectacular.utils import extend_schema

from .models import Guide
from .serializers import GuideSerializer

from rest_framework import generics


@extend_schema(tags=['Guides'])
class GuideDetailView(generics.RetrieveAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
