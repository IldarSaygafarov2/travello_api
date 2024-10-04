from drf_spectacular.utils import extend_schema
from rest_framework import generics, viewsets
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response

from helpers.main import send_message_to_channel
from .models import StaticMediaContent, ServiceWorkingStep, Tag
from .serializers import NewsletterSerializer, StaticMediaContentSerializer, ServiceWorkingStepSerializer, TagSerializer
from constance import config


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


class ContactsPageMapView(generics.GenericAPIView):
    renderer_classes = [StaticHTMLRenderer]

    def get(self, request):
        return Response(config.MAP_CODE)

    def display_contacts_page_map(request):
        _map = """
<div style="position:relative;overflow:hidden;"><a href="https://yandex.uz/maps/org/185069300267/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">PROWEB</a><a href="https://yandex.uz/maps/10335/tashkent/category/educational_center/184106168/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:14px;">Учебный центр в Ташкенте</a><a href="https://yandex.uz/maps/10335/tashkent/category/courses_and_master_classes/184106220/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:28px;">Курсы и мастер-классы в Ташкенте</a><iframe src="https://yandex.uz/map-widget/v1/?ll=69.274386%2C41.297958&mode=poi&poi%5Bpoint%5D=69.273855%2C41.297669&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D185069300267&z=17.37" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>
    """
        return Response({
            'map': _map
        })
