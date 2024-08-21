from django.db import models
from apps.events.models import Event
from apps.users.models import User


# Create your models here.
class FavoriteTour(models.Model):
    tours = models.ForeignKey(Event, related_name='favorites', on_delete=models.CASCADE, verbose_name='Тур', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites', verbose_name='Пользователь', null=True, blank=True)

    def __str__(self):
        return f'{self.user}: {self.tours}'

    class Meta:
        verbose_name = 'Избранный тур'
        verbose_name_plural = 'Избранные туры'