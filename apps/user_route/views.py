from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import (
    UserTourRoute,
)
from .serializers import (
    UserRouteSerializer,
    UserRouteCreateSerializer
)


@extend_schema(tags=['Users'])
class UserTourRouteView(generics.ListAPIView):
    queryset = UserTourRoute.objects.all()
    serializer_class = UserRouteSerializer


@extend_schema(tags=['Users'])
class UserTourCreateView(generics.CreateAPIView):
    queryset = UserTourRoute.objects.all()
    serializer_class = UserRouteCreateSerializer
