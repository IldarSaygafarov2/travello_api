from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model."""
    phone_number = models.CharField(verbose_name='Номер телефона', unique=True, max_length=15, null=True)
    surname = models.CharField(verbose_name='Отчество', max_length=30, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(verbose_name='Пол', max_length=10, null=True)
    verification_code = models.CharField(max_length=6, null=True)
    is_verified = models.BooleanField(default=False)


class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Passport(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    lastname = models.CharField(verbose_name='Фамилия', max_length=100)
    surname = models.CharField(verbose_name='Отчество', max_length=100)
    birth_date = models.DateField()
    seria = models.CharField(verbose_name='Серия', max_length=100)
    issued_by = models.CharField(verbose_name='Кем выдан', max_length=150)
    issued_date = models.DateField()
    citizen = models.CharField(verbose_name='Гражданство', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passport_data', verbose_name='Пользователь')

    def __str__(self):
        return f'{self.lastname} {self.first_name} {self.surname}: {self.seria}'

    class Meta:
        verbose_name = 'Паспортные данные'
        verbose_name_plural = 'Паспортные данные'


class Tourist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tourist', null=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    lastname = models.CharField(max_length=100, verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата рождения')
    gender = models.CharField(verbose_name='Гендер', max_length=20)
    passport_seria_and_number = models.CharField(max_length=20, verbose_name='Серия и номер паспорта')
    expiration_date = models.DateField(verbose_name='Дата окончания паспорта')
    citizen = models.CharField(verbose_name='Гражданство', max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.lastname}'

    class Meta:
        verbose_name = 'Турист'
        verbose_name_plural = 'Туристы'


class Children(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children', null=True)
    fullname = models.CharField(verbose_name='Полное имя', max_length=100)
    gender = models.CharField(verbose_name='Гендер', max_length=100)
    birth_date = models.DateField(verbose_name='Дата рождения')
    birth_certificate = models.FileField(verbose_name='Свидетельство о рождении',
                                         upload_to='users/children/birth_certificates/')

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'
