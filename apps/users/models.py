from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class UserTypeChoices(models.TextChoices):
    GUIDE = 'guide', 'Гид'
    TRANSPORT_WORKER = 'transport_worker', 'Транспортник'

    __empty__ = 'Неизвестно'


class User(AbstractUser):
    """Custom User model."""
    phone_number = models.CharField(verbose_name='Номер телефона', unique=True, max_length=15, null=True, blank=True)
    surname = models.CharField(verbose_name='Отчество', max_length=30, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=10, null=True, blank=True)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    user_type = models.CharField(verbose_name='Тип пользователя', max_length=100, choices=UserTypeChoices.choices,
                                 null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.user_type == 'guide' or self.user_type == 'transport_worker':
            self.is_staff = True
            self.user_permissions.add()

        super().save(*args, **kwargs)


class UserTemp(models.Model):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    verification_code = models.CharField(max_length=4, null=True, blank=True)
    data = models.JSONField()


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
    first_name = models.CharField(max_length=100, verbose_name='Имя', null=True)
    lastname = models.CharField(max_length=100, verbose_name='Фамилия', null=True)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True)
    gender = models.CharField(verbose_name='Гендер', max_length=20, null=True)
    passport_seria_and_number = models.CharField(max_length=20, verbose_name='Серия и номер паспорта', null=True)
    expiration_date = models.DateField(verbose_name='Дата окончания паспорта', null=True)
    citizen = models.CharField(verbose_name='Гражданство', max_length=100, null=True)

    def __str__(self):
        return f'{self.first_name} {self.lastname}'

    def display_reverse_url(self):
        return reverse('users:tourist-list', kwargs={'user_pk': self.pk})

    class Meta:
        verbose_name = 'Турист'
        verbose_name_plural = 'Туристы'


class Children(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children', null=True)
    fullname = models.CharField(verbose_name='Полное имя', max_length=100)
    gender = models.CharField(verbose_name='Гендер', max_length=100, null=True)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True)
    birth_certificate = models.FileField(verbose_name='Свидетельство о рождении',
                                         upload_to='users/children/birth_certificates/', null=True)

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'


class UserHotelSearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hotels_history', null=True)
    country_from = models.CharField(max_length=100, verbose_name='Откуда')
    country_to = models.CharField(max_length=100, verbose_name='Куда')
    departure_date = models.DateField(verbose_name='Дата вылета')
    nights = models.PositiveSmallIntegerField(verbose_name='Кол-во ночей')
    passengers = models.PositiveSmallIntegerField(verbose_name='Кол-во пассажиров')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'История поиска тура'
        verbose_name_plural = 'История поиска туров'
