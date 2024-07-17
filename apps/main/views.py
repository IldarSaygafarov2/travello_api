from django.conf import settings
from django.core import mail
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.response import Response
from . import messages
from .serializers import NewsletterSerializer


@extend_schema(tags=['Common'])
class NewsletterView(generics.GenericAPIView):
    serializer_class = NewsletterSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        mail.send_mail(
            subject='Вопрос пользователя',
            message=messages.NEWSLETTER_MESSAGE.format(
                name=data['name'],
                email=data['email'],
                text=data['text'],
            ),
            from_email=data['email'],
            recipient_list=[settings.EMAIL_HOST_USER],
        )
        return Response({'is_send': True})

