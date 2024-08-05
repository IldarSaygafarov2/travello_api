from django.db import models
from apps.events.models import Event


class Hotel(models.Model):
    class HotelRatingChoices(models.IntegerChoices):
        ONE = 1, 1
        TWO = 2, 2
        THREE = 3, 3
        FOUR = 4, 4
        FIVE = 5, 5

    name = models.CharField(max_length=500, verbose_name='Название отеля')
    preview = models.ImageField(upload_to='images/hotels/previews/', verbose_name='Превью фото')
    country = models.CharField(verbose_name='Страна', max_length=255)
    address = models.CharField(verbose_name='Адрес', max_length=500)
    short_description = models.TextField(verbose_name='Описание')
    rating = models.IntegerField(verbose_name='Рейтинг отеля', choices=HotelRatingChoices.choices,
                                 default=HotelRatingChoices.FIVE)
    distance_to_beach = models.IntegerField(verbose_name='Расстояние до пляжа')
    price = models.IntegerField(verbose_name='Цена')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

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



