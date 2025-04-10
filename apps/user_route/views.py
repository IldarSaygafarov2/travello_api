from datetime import datetime
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.response import Response

from apps.users.models import User, Tourist
from apps.users.serializers import TouristSerializer
from .models import (
    UserTourRoute,
    UserTourHotel,
    UserTourTransport,
    UserRouteAdditionalService,
)
from .serializers import (
    UserRouteSerializer,
    UserRouteCreateSerializer,
    UserTourHotelSerializer,
    UserTourTransportSerializer,
    UserRouteAdditionalServiceSerializer,
)
from travello import settings
import requests
from ..hotels.models import Hotel, HotelRoom


@extend_schema(tags=["Users"])
class UserTourRouteView(generics.ListAPIView):
    queryset = UserTourRoute.objects.all()
    serializer_class = UserRouteSerializer


@extend_schema(tags=["Users"])
class UserTourCreateView(generics.CreateAPIView):
    queryset = UserTourRoute.objects.all()
    serializer_class = UserRouteCreateSerializer

    def create(self, request, *args, **kwargs):
        # TODO: закончить добавление данных от конструктора
        user_id = kwargs.get("pk")

        data = request.data

        tourists = data.pop("tourists")
        hotels = data.pop("hotels")
        transports = data.pop("transports")
        guides = data.pop("guides")
        additional_services = data.pop("additional_services")

        user = User.objects.get(pk=user_id)

        data["user"] = user.pk

        tourists_data = []
        for tourist in tourists:
            tourist["user"] = user
            obj = Tourist.objects.create(**tourist)
            obj.save()
            tourists_serializer = TouristSerializer(obj, many=False)
            tourists_data.append(tourists_serializer.data)

        user_route_serializer = self.serializer_class(data=data)
        user_route_serializer.is_valid(raise_exception=True)
        user_route_serializer.save()
        user_route_data = user_route_serializer.data

        user_route_obj = UserTourRoute.objects.get(pk=user_route_data["id"])

        user_route_data["tourists"] = tourists_data
        hotels_data = []
        transport_data = []
        service_data = []
        for hotel in hotels:
            hotel_obj = Hotel.objects.get(pk=hotel["hotel"])
            room_obj = HotelRoom.objects.get(pk=hotel["room"])

            hotel["user_route"] = user_route_obj
            hotel["hotel"] = hotel_obj
            hotel["room"] = room_obj

            obj = UserTourHotel.objects.create(**hotel)
            obj.save()

            user_hotels_serializer = UserTourHotelSerializer(obj, many=False)
            hotels_data.append(user_hotels_serializer.data)

        for transport in transports:
            transport["user_route"] = user_route_obj

            transport_obj = UserTourTransport.objects.create(**transport)
            transport_obj.save()

            user_transport_serializer = UserTourTransportSerializer(
                transport_obj, many=False
            )
            transport_data.append(user_transport_serializer.data)

        for service in additional_services:
            service["user_route"] = user_route_obj
            service_obj = UserRouteAdditionalService.objects.create(**service)
            service_obj.save()

            user_service_serializer = UserRouteAdditionalServiceSerializer(
                service_obj, many=False
            )
            service_data.append(user_service_serializer.data)

        user_route_data["hotels"] = hotels_data
        user_route_data["transports"] = transport_data
        user_route_data["additional_services"] = service_data

        tg_messages = "Бронь тура(Конструктор)\n\n"
        tg_messages = f"Дата брони: {user_route_data['created_at']}\n\n"

        tg_messages += f"{user.get_full_name()}\n{user.phone_number} / {user.email}\n\n"
        tg_messages += f'Кол-во туристов: {len(user_route_data["tourists"])}\n\n'
        tg_messages += f'Отель: {", ".join([Hotel.objects.get(pk=int(obj.get('hotel'))).name for obj in hotels_data])}\n'
        tg_messages += f'Номер: {", ".join([HotelRoom.objects.get(pk=int(obj.get('room'))).name for obj in hotels_data])}\n\n'

        tg_messages += f"{settings.API_URL_MAIN}/admin/user_route/usertourroute/{user_route_data['id']}/change/"
        requests.post(
            url=settings.TG_API_URL.format(
                token=settings.MAIN_BOT_TOKEN,
                channel_id=settings.CONSTRUCTOR_CHANNEL,
                text=tg_messages,
            )
        )
        return Response(user_route_data, status=201)


"""
Бронь тура(Конструктов)

ФИО

Номер телефона / email

Кол-во туристов: 
Отель: 
Номер: 

Ссылка на фулл данные
{
  "id": 10,
  "user": 14,
  "tourists": [
    {
      "id": 29,
      "user": 14,
      "first_name": "tourist 1",
      "lastname": "tourist 1",
      "birth_date": "2024-11-14",
      "passport_seria_and_number": "ab312311",
      "expiration_date": "2024-11-14",
      "gender": "male",
      "citizen": "uzbekistan"
    }
  ],
  "hotels": [
    {
      "user_route": 10,
      "hotel": 1,
      "room": 1
    }
  ],
  "transports": [
    {
      "user_route": 10,
      "transport_type": "group",
      "transfer_type": "type 1",
      "from_to": "hotel",
      "hotel_details": "some hotel",
      "number_of_tourists": 3
    }
  ],
  "additional_services": [
    {
      "user_route": 10,
      "photo_video_shooting": true,
      "open_sim_card": false
    }
  ]
}
"""

"""
{
    "user": 0,
    "tourists": [
        {
            "user": 0,
            "first_name": "tourist 1",
            "lastname": "tourist 1",
            "birth_date": "2024-11-14",
            "passport_seria_and_number": "ab312311",
            "expiration_date": "2024-11-14",
            "gender": "male",
            "citizen": "uzbekistan"
        }
    ],
    "hotels": [
        {
            "user_route": 0,
            "hotel": 325,
            "room": 546
        }
    ],
    "transports": [
        {
            "user_route": 0,
            "transport_type": "group",
            "transfer_type": "type 1",
            "from_to": "hotel",
            "hotel_details": "some hotel",
            "number_of_tourists": 3
        }
    ],
    "guides": [
        {
            "user_route": 0,
            "guide": 1
        }
    ],
    "additional_services": [
        {
            "user_route": 0,
            "photo_video_shooting": true,
            "open_sim_card": false
        }
    ]
}
"""
