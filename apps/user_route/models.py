from django.db import models

from apps.hotels.models import Hotel, HotelRoom
from apps.users.models import User


class UserTourRoute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')


class UserTourHotel(models.Model):
    user_route = models.ForeignKey(UserTourRoute, on_delete=models.CASCADE, related_name='user_route')
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, related_name='user_tour_route', null=True)
    room = models.ForeignKey(HotelRoom, on_delete=models.SET_NULL, null=True)


class UserTourTransport(models.Model):
    class TransportTypeChoices(models.TextChoices):
        GROUP = 'group', 'Групповой'
        INDIVIDUAL = 'individual', 'Индивидуальный'

        __empty__ = ''

    user_route = models.ForeignKey(UserTourRoute, on_delete=models.CASCADE, related_name='user_transport')
    transport_type = models.CharField(verbose_name='Тип транспорта', max_length=50,
                                      choices=TransportTypeChoices.choices,
                                      null=True, blank=True)
    transfer_type = models.CharField(verbose_name='Тип трансфера', max_length=150)
    from_to = models.CharField(verbose_name='Откуда куда', max_length=250)
    hotel_details = models.CharField(verbose_name='Данные гостиницы', max_length=500)
    number_of_tourists = models.IntegerField(verbose_name='Количество туристов')
