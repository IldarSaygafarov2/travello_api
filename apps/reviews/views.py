from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import Review
from .serializers import ReviewSerializer, ReviewCreateSerializer


@extend_schema(tags=["Reviews"])
class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("user_type", "hotel")


@extend_schema(tags=["Reviews"])
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
