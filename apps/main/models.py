from django.db import models


class Newsletter(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя отправителя')
    email = models.EmailField(verbose_name='Почта отправителя')
    text = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        verbose_name = 'Вопрос пользователя'
        verbose_name_plural = 'Вопросы пользователя'

