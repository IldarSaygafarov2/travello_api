from django.db import models

from apps.users.models import User


class Guide(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Гид'
        verbose_name_plural = 'Гиды'