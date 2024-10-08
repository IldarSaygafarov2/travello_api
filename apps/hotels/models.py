from django.db import models
from django.utils.translation import gettext as _
from apps.events.models import Event
from django.template.defaultfilters import slugify


class HotelStarsChoices(models.IntegerChoices):
    ONE = 1, '1'
    TWO = 2, '2'
    THREE = 3, '3'
    FOUR = 4, '4'
    FIVE = 5, '5'


class HotelRatingChoices(models.TextChoices):
    FOUR_POINT_FIVE = 'four_five', '4.5+'
    FOUR = 'four', '4+'
    THREE = 'three', '3+'


class HotelTypeOfAllocation(models.TextChoices):
    APART_HOTEL = 'apart_hotel', _('Апарт-отель')
    APARTMENTS = 'apartments', _('Апартаменты')
    VILLA = 'villa', _('Вилла')
    COTTAGE = 'cottage', _('Котедж')
    HOTEL = 'hotel', _('Отель')
    HOSTEL = 'hostel', _('Хостел')


class HotelBeachLineChoices(models.TextChoices):
    FIRST = 'first', _('Первая')
    SECOND = 'second', _('Вторая')
    THIRD = 'third', _('Третья')


class HotelBeachTypeChoices(models.TextChoices):
    SAND = 'sand', _('Песок')
    PEBBLE = 'pebble', _('Галька')
    PLATFORM = 'platform', _('Платформа')


class HotelFoodChoices(models.TextChoices):
    ALL_INCLUSIVE = 'all_inclusive', _('Все включено')
    WITHOUT_FOOD = 'without_food', _('Без питания')
    LUNCH_DINNER = 'lunch_dinner', _('Обед и ужин')
    BREAKFAST_LUNCH_DINNER = 'breakfast_lunch_dinner', _('Завтрак, обед или ужин')

    __empty__ = ''


class HotelFacilitiesChoices(models.TextChoices):
    BAR = 'bar', _("Бар")
    AIR_CONDITIONER = 'air_conditioner', _('Кондиционер')
    SPA = 'spa', _('Спа')
    PARKING = 'parking', _('Парковка')

    __empty__ = ''


class Hotel(models.Model):
    name = models.CharField(max_length=500, verbose_name='Название отеля')
    slug = models.SlugField(null=True, verbose_name='Слаг')
    preview = models.ImageField(upload_to='images/hotels/previews/', verbose_name='Превью фото')
    country = models.CharField(verbose_name='Страна', max_length=255)
    city = models.CharField(verbose_name='Город', max_length=100, null=True, blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=500)
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')
    stars = models.IntegerField(verbose_name='Кол-во звёзд отеля', choices=HotelStarsChoices.choices,
                                default=HotelStarsChoices.FIVE)
    rating = models.CharField(max_length=15, choices=HotelRatingChoices.choices,
                              default=HotelRatingChoices.FOUR_POINT_FIVE, verbose_name='Рейтинг')
    distance_to_airport = models.IntegerField(verbose_name='Расстояние до аэропорта, км')
    latitude = models.FloatField(verbose_name='Широта', null=True, blank=True)
    longitude = models.FloatField(verbose_name='Долгота', null=True, blank=True)
    nights = models.IntegerField(verbose_name='Кол-во ночей', default=0)
    total_people = models.IntegerField(verbose_name='Кол-во человек', default=0)
    has_wifi = models.BooleanField(default=True, verbose_name='Есть вай-фай?')
    is_meals_included = models.BooleanField(verbose_name='Питание включено?', default=True)
    allocation_type = models.CharField(max_length=50, verbose_name='Тип размещения',
                                       choices=HotelTypeOfAllocation.choices, null=True, blank=True)
    beach_line = models.CharField(choices=HotelBeachLineChoices.choices, max_length=50, verbose_name='Линия пляжа',
                                  null=True, blank=True)
    beach_type = models.CharField(choices=HotelBeachTypeChoices.choices, max_length=50, verbose_name='Тип пляжа',
                                  null=True, blank=True)
    food_type = models.CharField(choices=HotelFoodChoices.choices, max_length=50, null=True, blank=True)
    facility = models.CharField(choices=HotelFacilitiesChoices.choices, max_length=50, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_hotes', null=True, blank=True,
                              verbose_name='Тур')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class HotelBooking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_booking', verbose_name='Отель')
    hotel_room = models.ForeignKey('HotelRoom', on_delete=models.CASCADE, related_name='hotel_booking',
                                   verbose_name='Номер отеля')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_hotel', verbose_name='Тур')
    total_adult = models.PositiveIntegerField(verbose_name='Количество отдыхающих', default=0)
    total_children = models.PositiveIntegerField(verbose_name='Количество детей', default=0)

    def __str__(self):
        return f'{self.hotel} - {self.event}'

    class Meta:
        verbose_name = 'Бронь отеля'
        verbose_name_plural = 'Брони отелей'


def gallery_image_path(instance, filename):
    return f'images/hotels/{instance.hotel.name}/{filename}'


class HotelGallery(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_gallery', verbose_name='Отель')
    photo = models.ImageField(upload_to=gallery_image_path, verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото отеля'
        verbose_name_plural = 'Фотки отеля'


class HotelFacility(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Отель', related_name='facilities')
    name = models.CharField(verbose_name='Удобство', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Удобство отеля'
        verbose_name_plural = 'Удобства отеля'


class HotelEntertainment(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='entertainment', verbose_name='Отель')
    name = models.TextField(verbose_name='Развлечение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Развлечение'
        verbose_name_plural = 'Развлечения'


class HotelRoom(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Отель', related_name='rooms')
    name = models.CharField(verbose_name='Название номера', max_length=255)
    is_all_inclusive = models.BooleanField(default=True, verbose_name='Все включено?')
    description = models.TextField(verbose_name='Удобства в номере')
    nights = models.IntegerField(verbose_name='Кол-во ночей')
    price = models.IntegerField(verbose_name='Цена')
    until = models.DateField(verbose_name='До')

    def __str__(self):
        return f'{self.hotel.name}: {self.name}'

    class Meta:
        verbose_name = 'Номер в отеле'
        verbose_name_plural = 'Номера в отеле'


def hotel_room_image_path(instance, filename):
    return f'images/hotels/{instance.room.hotel.name}/{instance.room.name}/{filename}'


class HotelRoomImages(models.Model):
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='room_images',
                             verbose_name='Номер отеля')
    image = models.ImageField(verbose_name='Фото номера', upload_to=hotel_room_image_path, blank=True, null=True)

    class Meta:
        verbose_name = 'Фото номера'
        verbose_name_plural = 'Фото номера'


class HotelRoomFacilities(models.Model):
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='room_facilities',
                             verbose_name='Номер отеля')
    facility = models.CharField(verbose_name='Удобство', max_length=255)

    def __str__(self):
        return self.facility

    class Meta:
        verbose_name = 'Удобство номера'
        verbose_name_plural = 'Удобства номера'
