from django.db import models
from django.utils.translation import gettext as _
from apps.events.models import Event


class HotelRatingChoices(models.IntegerChoices):
    ONE = 1, '1'
    TWO = 2, '2'
    THREE = 3, '3'
    FOUR = 4, '4'
    FIVE = 5, '5'


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


class Hotel(models.Model):
    name = models.CharField(max_length=500, verbose_name='Название отеля')
    preview = models.ImageField(upload_to='images/hotels/previews/', verbose_name='Превью фото')
    country = models.CharField(verbose_name='Страна', max_length=255)
    city = models.CharField(verbose_name='Город', max_length=100, null=True, blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=500)
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')
    rating = models.IntegerField(verbose_name='Рейтинг отеля', choices=HotelRatingChoices.choices,
                                 default=HotelRatingChoices.FIVE)
    distance_to_beach = models.IntegerField(verbose_name='Расстояние до пляжа, м')
    distance_to_airport = models.IntegerField(verbose_name='Расстояние до аэропорта, км')
    price = models.IntegerField(verbose_name='Цена')
    latitude = models.FloatField(verbose_name='Широта', null=True, blank=True)
    longitude = models.FloatField(verbose_name='Долгота', null=True, blank=True)
    nights = models.IntegerField(verbose_name='Кол-во ночей', default=0)
    total_people = models.IntegerField(verbose_name='Кол-во человек', default=0)
    has_wifi = models.BooleanField(default=True, verbose_name='Есть вай-фай?')
    is_meals_included = models.BooleanField(verbose_name='Питание включено?', default=True)
    allocation_type = models.CharField(max_length=50, verbose_name='Тип размещения',
                                       choices=HotelTypeOfAllocation.choices, default=HotelTypeOfAllocation.APART_HOTEL)
    beach_line = models.CharField(choices=HotelBeachLineChoices.choices, max_length=50,
                                  default=HotelBeachLineChoices.FIRST, verbose_name='Линия пляжа')
    beach_type = models.CharField(choices=HotelBeachTypeChoices.choices, max_length=50,
                                  default=HotelBeachTypeChoices.SAND, verbose_name='Тип пляжа')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_hotes', null=True, blank=True,
                              verbose_name='Тур')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


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
