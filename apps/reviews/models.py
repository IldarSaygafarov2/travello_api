from django.db import models
from apps.events.models import Event
from apps.hotels.models import Hotel


class Review(models.Model):
    class UserTypeChoices(models.TextChoices):
        SIMPLE = 'simple', 'Физ лицо'
        ADVANCED = 'advanced', 'Юр лицо'

        __empty__ = ''

    class ReviewTypeChoices(models.TextChoices):
        TOUR = 'tour', 'Отзыв для тура'
        HOTEL = 'hotel', 'Отзыв для отеля'
        COMMON = 'common', 'Обычный отзыв'

    fullname = models.CharField(max_length=150, verbose_name='Имя', null=True, blank=True)
    avatar = models.URLField(verbose_name='Ссылка на фото', null=True, blank=True)
    text = models.TextField(verbose_name='Текст отзыва')
    user_type = models.CharField(verbose_name='Тип пользователя', choices=UserTypeChoices.choices, null=True,
                                 blank=True,
                                 max_length=20)
    review_type = models.CharField(max_length=50, choices=ReviewTypeChoices.choices, default=ReviewTypeChoices.COMMON,
                                   verbose_name='Тип отзыва')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True,
                              verbose_name='Тур')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True,
                              verbose_name='Отель')

    def __str__(self):
        return f'Отзыв от {self.fullname}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
