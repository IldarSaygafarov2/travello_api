from django.db import models

from apps.hotels.models import Hotel, HotelRoom
from apps.roles.models import Guide, GuideTour
from apps.users.models import User


class UserTourRoute(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"

    class Meta:
        verbose_name = "Тур пользователя"
        verbose_name_plural = "Туры пользователя"


class UserTourHotel(models.Model):
    user_route = models.ForeignKey(
        UserTourRoute, on_delete=models.CASCADE, related_name="user_route"
    )
    hotel = models.ForeignKey(
        Hotel, on_delete=models.SET_NULL, related_name="user_tour_route", null=True
    )
    room = models.ForeignKey(HotelRoom, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"


class UserTourTransport(models.Model):
    class TransportTypeChoices(models.TextChoices):
        GROUP = "group", "Групповой"
        INDIVIDUAL = "individual", "Индивидуальный"

        __empty__ = ""

    user_route = models.ForeignKey(
        UserTourRoute, on_delete=models.CASCADE, related_name="user_transport"
    )
    transport_type = models.CharField(
        verbose_name="Тип транспорта",
        max_length=50,
        choices=TransportTypeChoices.choices,
        null=True,
        blank=True,
    )
    transfer_type = models.CharField(verbose_name="Тип трансфера", max_length=150)
    from_to = models.CharField(verbose_name="Откуда куда", max_length=250)
    hotel_details = models.CharField(verbose_name="Данные гостиницы", max_length=500)
    number_of_tourists = models.IntegerField(verbose_name="Количество туристов")

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорты"


class UserRouteGuide(models.Model):
    user_route = models.ForeignKey(
        UserTourRoute, on_delete=models.CASCADE, related_name="user_guide"
    )
    guide = models.ForeignKey(Guide, on_delete=models.SET_NULL, null=True)
    guide_route = models.ForeignKey(GuideTour, on_delete=models.SET_NULL, null=True)
    date_from = models.DateField(null=True)
    date_to = models.DateField(null=True)

    class Meta:
        verbose_name = "Гид"
        verbose_name_plural = "Гиды"


class UserRouteAdditionalService(models.Model):
    user_route = models.ForeignKey(
        UserTourRoute, on_delete=models.CASCADE, related_name="user_additional_service"
    )
    photo_video_shooting = models.BooleanField(default=False)
    open_sim_card = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Дополнительная услуга"
        verbose_name_plural = "Дополнительные услуги"
