from drf_spectacular.utils import extend_schema
from rest_framework import generics, viewsets
from rest_framework.response import Response

from helpers.main import send_message_to_channel
from .models import StaticMediaContent, ServiceWorkingStep, Tag
from .serializers import NewsletterSerializer, StaticMediaContentSerializer, ServiceWorkingStepSerializer, TagSerializer


@extend_schema(tags=['Common'])
class ServiceWorkingStepList(generics.ListAPIView):
    serializer_class = ServiceWorkingStepSerializer
    queryset = ServiceWorkingStep.objects.all()


@extend_schema(tags=['Common'])
class TagListView(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


@extend_schema(tags=['Common'])
class NewsletterView(generics.GenericAPIView):
    serializer_class = NewsletterSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_message_to_channel(
            name=serializer.data['name'],
            email=serializer.data['email'],
            message=serializer.data['text']
        )
        return Response({'is_send': True})


@extend_schema(tags=['Common'])
class StaticMediaContentView(viewsets.ModelViewSet):
    serializer_class = StaticMediaContentSerializer
    queryset = StaticMediaContent.objects.all()
    lookup_field = 'page_slug'
    lookup_url_kwarg = 'page_slug'