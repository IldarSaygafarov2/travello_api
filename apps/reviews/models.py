from django.db import models


class Review(models.Model):
    class UserTypeChoices(models.TextChoices):
        SIMPLE = 'simple', 'Физ лицо'
        ADVANCED = 'advanced', 'Юр лицо'

        __empty__ = ''

    fullname = models.CharField(max_length=150, verbose_name='Имя', null=True, blank=True)
    avatar = models.URLField(verbose_name='Ссылка на фото', null=True, blank=True)
    text = models.TextField(verbose_name='Текст отзыва')
    user_type = models.CharField(verbose_name='Тип пользователя', choices=UserTypeChoices.choices, null=True, blank=True,
                                 max_length=20)

    def __str__(self):
        return f'Отзыв от {self.fullname}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
