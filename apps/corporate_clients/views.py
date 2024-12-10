import requests
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from helpers.telegram import msg_for_corporate_client_request, get_documents_urls
from travello import settings
from .models import CorporateClientRequest, OurClient
from .serializers import CorporateClientRequestSerializer, OurClientSerializer


@extend_schema(tags=["Corporate Clients"])
class CorporateClientRequestView(generics.CreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset = CorporateClientRequest.objects.all()
    serializer_class = CorporateClientRequestSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs).data
        documents_urls = get_documents_urls(data)
        msg = msg_for_corporate_client_request(data)
        res = requests.post(
            url=settings.TG_API_URL.format(
                token=settings.MAIN_BOT_TOKEN,
                channel_id=settings.CORPORATE_CLIENTS_CHANNEL,
                text=msg,
            )
        )
        for field_name, url in documents_urls:
            r = requests.post(
                url=settings.TG_SEND_DOCUMENT_URL.format(
                    token=settings.MAIN_BOT_TOKEN,
                    channel_id=settings.CORPORATE_CLIENTS_CHANNEL,
                    document=url,
                    caption=field_name,
                )
            )
            print(r.json())
        # print(res.json())
        return Response(data)


@extend_schema(tags=["Corporate Clients"])
class OurClientView(generics.ListAPIView):
    queryset = OurClient.objects.all()
    serializer_class = OurClientSerializer
