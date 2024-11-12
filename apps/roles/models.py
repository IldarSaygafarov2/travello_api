from django.db import models

from apps.users.models import User
from helpers.main import make_tuple_choices

LANGUAGES_CHOICES = make_tuple_choices('langs.json')


class ModeOfTransportationChoices(models.TextChoices):
    ON_FOOT = 'on_foot', 'Пешком'
    BY_CAR = 'by_car', 'На авто'
    INDOORS = 'indoors', 'В помещении'
    BY_BIKE = 'by_bike', 'На велосипеде'
    BY_BUS = 'by_bus', 'На автобусе'
    ON_A_MOTORCYCLE = 'on_a_motorcycle', 'На мотоцикле'
    ON_THE_SHIP = 'on_the_ship', 'На корабле'
    OTHER = 'other', 'Другое (впишу сам)'

    __empty__ = ''


class TourDurationChoices(models.TextChoices):
    HALF_OUR = 'half_our', 'Пол часа'
    HOUR = 'hour', 'Час'
    ONE_AND_HALF_OUR = 'one_and_half_our', '1,5 часа'

    __empty__ = ''


class NumberOfPeopleChoices(models.TextChoices):
    WITH_CHILDREN = 'with_children', 'Можно с детьми'
    PAY_FOR_CHILDREN = 'pay_for_children', 'Доплата за ребенка'

    __empty__ = ''


class WorkingWithOrders(models.TextChoices):
    HALF_OUR = 'half_our', 'За пол часа'
    HOUR = 'hour', 'За час'
    ANY_TIME = 'any_time', 'Можно бронировать в любой момент'

    __empty__ = ''


class Guide(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        null=True, blank=True
    )
    about_me = models.TextField(verbose_name='О гиде', null=True, blank=True)
    avatar = models.ImageField(
        verbose_name='Фото гида',
        upload_to='guides/avatars/',
        null=True,
        blank=True
    )
    experience = models.IntegerField(verbose_name='Стаж', null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена за тур', null=True, blank=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Гид'
        verbose_name_plural = 'Гиды'


class GuideLanguage(models.Model):
    guide = models.ForeignKey(
        Guide,
        on_delete=models.CASCADE,
        verbose_name='Гид',
        related_name='languages',
        null=True,
        blank=True
    )
    lang = models.CharField(verbose_name='Язык', max_length=50)

    def __str__(self):
        return self.lang

    class Meta:
        verbose_name = 'Язык гида'
        verbose_name_plural = 'Языки гида'


class GuideTour(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, verbose_name='Гид', related_name='routes')

    title = models.CharField(verbose_name='Название маршрута', max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    additional = models.TextField(verbose_name='Дополнительно', null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=100, null=True, blank=True)
    gathering_place = models.CharField(verbose_name='Место встречи', max_length=100, null=True, blank=True)
    language = models.CharField(verbose_name='Язык', max_length=250, null=True, blank=True)
    duration = models.CharField(verbose_name='Длительность маршрута', max_length=150, null=True, blank=True)
    participants_number = models.CharField(verbose_name='Количество участников', max_length=150, null=True, blank=True)
    transportation_type = models.CharField(verbose_name='Способ передвижения', blank=True, null=True, max_length=100,
                                           choices=ModeOfTransportationChoices.choices)
    price = models.IntegerField(verbose_name='Цена')
    working_with_orders = models.CharField(verbose_name='Работа с заказами',
                                           choices=WorkingWithOrders.choices, max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Маршрут гида'
        verbose_name_plural = 'Маршруты гидов'


class GuideTourExpectation(models.Model):
    guide_tour = models.ForeignKey(
        GuideTour, on_delete=models.CASCADE, verbose_name='Маршрут', related_name='expectations')
    text = models.TextField(verbose_name='Ожидание туриста')

    def __str__(self):
        return str(self.text)[:255] + '...'


class GuideTourOrganizationalDetail(models.Model):
    guide_tour = models.ForeignKey(
        GuideTour, on_delete=models.CASCADE, verbose_name='Маршрут гида', related_name='organizational_details')
    text = models.TextField(verbose_name='Текст')


class GuideSchedule(models.Model):
    guide_tour = models.ForeignKey(
        GuideTour, on_delete=models.CASCADE, verbose_name='Маршрут тура', related_name='schedules')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')

    def __str__(self):
        return f'{self.date} {self.time}'

    class Meta:
        verbose_name = 'Расписание гида'
        verbose_name_plural = 'Расписания гидов'


class GuideTourPhoto(models.Model):
    guide_tour = models.ForeignKey(
        GuideTour, on_delete=models.CASCADE, verbose_name='Маршрут тура', related_name='photos')
    image = models.ImageField(
        verbose_name='Фото тура', upload_to='guides/routes/tours/', blank=True, null=True
    )


class GuidePassport(models.Model):
    guide = models.OneToOneField(Guide, on_delete=models.CASCADE, verbose_name='Гид', related_name='passports')
    seria_and_number = models.CharField(verbose_name='Серия и номер', max_length=100, unique=True,
                                        blank=True,
                                        null=True)
    issued_date = models.DateField(
        verbose_name='Дата выдачи',
        blank=True,
        null=True
    )
    issued_by = models.CharField(verbose_name='Кем выдан', max_length=100, blank=True,
                                 null=True)
    citizen = models.CharField(verbose_name='Гражданство', max_length=100, blank=True,
                               null=True)
    agree_to_save_data = models.BooleanField(verbose_name='Согласен на сохранение паспортных данных', blank=True,
                                             null=True)
    ready_for_trip = models.BooleanField(verbose_name='Готов к международным поездкам', blank=True,
                                         null=True)

    def __str__(self):
        return f'{self.guide.user.first_name}'

    class Meta:
        verbose_name = 'Паспорт гида'
        verbose_name_plural = 'Паспортные данные гида'

