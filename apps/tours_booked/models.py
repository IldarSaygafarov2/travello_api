from django.db import models

from apps.events.models import Event, EventType
from apps.users.models import User


# Create your models here.

class EventBooking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_booking', verbose_name='Тур')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_booking', verbose_name='Пользователь')
    event_type = models.CharField(verbose_name='Тип тура', max_length=20, choices=EventType.choices,
                                  default=EventType.WORLD, null=True, blank=True)
    total_adult = models.SmallIntegerField(verbose_name='Кол-во отдыхающих')
    total_children = models.SmallIntegerField(verbose_name='Кол-во детей')

    def __str__(self):
        return f'Бронь тура: {self.event} пользователем: {self.user}'

    class Meta:
        verbose_name = 'Бронь тура'
        verbose_name_plural = 'Брони туров'
