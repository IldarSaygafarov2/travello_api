import requests
from drf_spectacular.utils import extend_schema
from rest_framework import generics, viewsets
from rest_framework.response import Response

from apps.events.models import Event
from apps.users.models import Tourist, User
from travello import settings
from . import models, serializers, utils


@extend_schema(tags=["Events Booking"])
class EventBookingView(generics.ListCreateAPIView):
    serializer_class = serializers.EventBookingSerializer
    queryset = models.EventBooking.objects.all()
    lookup_url_kwarg = "event_id"

    def create(self, request, *args, **kwargs):
        data = request.data

        tourists = data["tourists"]

        user = User.objects.get(pk=data["user"])
        event = Event.objects.get(pk=data["event"])

        for tourist in tourists:
            obj, created = Tourist.objects.get_or_create(
                user=user,
                first_name=tourist["first_name"],
                lastname=tourist["lastname"],
                birth_date=tourist["birth_date"],
                passport_seria_and_number=tourist["passport_seria_and_number"],
                expiration_date=tourist["expiration_date"],
                gender=tourist["gender"],
                citizen=tourist["citizen"],
            )
            obj.save()

        new_book = models.EventBooking.objects.create(
            user=user,
            event=event,
            event_type=data["event_type"],
            total_adult=data["total_adult"],
            total_children=data["total_children"],
        )
        new_book.save()

        msg_obj = {
            "user": user.get_full_name(),
            "event": event.title,
            "total_adult": data["total_adult"],
            "total_children": data["total_children"],
            "event_type": new_book.get_event_type_display(),
            "tourists": tourists,
        }

        # print(tourists)

        msg = utils.create_event_booked_message(msg_obj)
        r = requests.post(
            url=settings.TG_API_URL.format(
                token=settings.MAIN_BOT_TOKEN,
                channel_id=settings.TOUR_BOOKINGS_CHANNEL,
                text=msg,
            )
        )
        print(r.json())
        return Response({"created": True})


@extend_schema(tags=["User Events Booking"])
class EventBookingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EventBookingSerializer
    queryset = models.EventBooking.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user_id=self.kwargs["user_pk"])
