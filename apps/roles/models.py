from django.db import models

from apps.users.models import User
from helpers.main import make_tuple_choices

LANGUAGES_CHOICES = make_tuple_choices('../../client/langs.json')


class Guide(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    about_me = models.TextField(verbose_name='О гиде', null=True, blank=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Гид'
        verbose_name_plural = 'Гиды'


class GuideLanguage(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, verbose_name='Гид', related_name='languages', null=True,
                              blank=True)
    lang = models.CharField(verbose_name='Язык', max_length=50)

    def __str__(self):
        return self.lang

    class Meta:
        verbose_name = 'Язык гида'
        verbose_name_plural = 'Языки гида'


class GuideTour(models.Model):
    class TourDurationChoices(models.TextChoices):
        HALF_OUR = 'half_our', 'Пол часа'
        HOUR = 'hour', 'Час'
        ONE_AND_HALF_OUR = 'one_and_half_our', '1,5 часа'

        __empty__ = ''

    class NumberOfPeopleChoices(models.TextChoices):
        WITH_CHILDREN = 'with_children', 'Можно с детьми'
        PAY_FOR_CHILDREN = 'pay_for_children', 'Доплата за ребенка'

        __empty__ = ''

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

    class WorkingWithOrders(models.TextChoices):
        HALF_OUR = 'half_our', 'За пол часа'
        HOUR = 'hour', 'За час'
        ANY_TIME = 'any_time', 'Можно бронировать в любой момент'

        __empty__ = ''

    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, verbose_name='Гид')
    title = models.CharField(verbose_name='Название маршрута', max_length=255)
    description = models.TextField(verbose_name='Описание программы')
    additional = models.TextField(verbose_name='Дополнительно')
    city = models.CharField(verbose_name='Город', max_length=255)
    gathering_place = models.TextField(verbose_name='Место встречи')
    language = models.CharField(verbose_name='Язык', max_length=50, choices=LANGUAGES_CHOICES, null=True, blank=True)
    tour_duration = models.CharField(verbose_name='Длительность проведения',
                                     choices=TourDurationChoices.choices, blank=True, null=True)
    number_of_people = models.CharField(verbose_name='Количество участников', choices=NumberOfPeopleChoices.choices,
                                        blank=True, null=True)
    mode_of_transportation = models.CharField(verbose_name='Способ передвижения',
                                              choices=ModeOfTransportationChoices.choices, blank=True, null=True)
    working_with_orders = models.CharField(verbose_name='Работа с заказами', choices=WorkingWithOrders.choices,
                                           blank=True, null=True, max_length=100)
    price = models.IntegerField(verbose_name='Цена', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Маршрут гида'
        verbose_name_plural = 'Маршруты гидов'


class GuideTourExpectation(models.Model):
    guide_tour = models.ForeignKey(GuideTour, on_delete=models.CASCADE, verbose_name='Маршрут')
    text = models.TextField(verbose_name='Ожидание туриста')

    def __str__(self):
        return str(self.text)[:255] + '...'


class GuideTourOrganizationalDetail(models.Model):
    guide_tour = models.ForeignKey(GuideTour, on_delete=models.CASCADE, verbose_name='Маршрут гида')
    text = models.TextField(verbose_name='Текст')


class GuideSchedule(models.Model):
    guide_tour = models.ForeignKey(GuideTour, on_delete=models.CASCADE, verbose_name='Маршрут тура')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')

    def __str__(self):
        return f'{self.date} {self.time}'

    class Meta:
        verbose_name = 'Расписание гида'
        verbose_name_plural = 'Расписания гидов'


class GuideTourPhoto(models.Model):
    guide_tour = models.ForeignKey(GuideTour, on_delete=models.CASCADE, verbose_name)