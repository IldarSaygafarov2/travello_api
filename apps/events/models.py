from ckeditor.fields import RichTextField
from django.db import models

from apps.users.models import Tourist, Children, User


class HotelRatingChoices(models.TextChoices):
    FOUR_POINT_FIVE = 'four_five', '4.5+'
    FOUR = 'four', '4+'
    THREE = 'three', '3+'


class EventType(models.TextChoices):
    WORLD = 'world', 'Мировой'
    LOCAL = 'uzbekistan', 'По узбекистану'

    __empty__ = '-'


def event_images_upload_to(instance, filename):
    return f'images/events/{instance.slug}/{filename}'


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название ивента (Тура)')
    slug = models.SlugField(verbose_name='Слаг',
                            help_text='Данное поле заполнять не нужно, оно заполняется автоматически', blank=True)
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')
    preview = models.ImageField(verbose_name='Фото', upload_to=event_images_upload_to, blank=True)
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    country_from = models.CharField(verbose_name='Страна вылета', max_length=100, default='Ташкент')
    country = models.CharField(verbose_name='Страна ивента', max_length=100)
    event_start = models.DateField(verbose_name='Число начала ивента')
    event_end = models.DateField(verbose_name='Число конца ивента')
    days = models.SmallIntegerField(verbose_name='Количество дней тура')
    nights = models.SmallIntegerField(verbose_name='Количество ночей тура')
    gathering_place = models.CharField(verbose_name='Место сбора группы', max_length=100)
    minimum_age = models.IntegerField(verbose_name='Минимальный возраст')
    people_in_group = models.IntegerField(verbose_name='Количество человек в группе')
    event_type = models.CharField(verbose_name='Тип тура', max_length=20, choices=EventType.choices,
                                  default=EventType.WORLD)
    rating = models.CharField(max_length=15, choices=HotelRatingChoices.choices,
                              default=HotelRatingChoices.FOUR_POINT_FIVE, verbose_name='Рейтинг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ивент'
        verbose_name_plural = 'Ивенты'


def event_images_gallery_upload_to(instance, filename):
    return f'images/events/{instance.event.slug}/gallery/{filename}'


class EventGallery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Ивент', related_name='images_gallery')
    image = models.ImageField(verbose_name='Фото', upload_to=event_images_gallery_upload_to, null=True, blank=True)
    slug = models.SlugField(default='', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.event.slug

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фото в галлерию'
        verbose_name_plural = 'Галлерея тура'


class EventTourProgram(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    day = models.IntegerField(verbose_name='День', help_text='День тура, например: "1 день, 2 день"')
    description = RichTextField(verbose_name='Описание')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tour_program')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'День программы тура'
        verbose_name_plural = 'Дни программы тура'


class EventTourProgramGallery(models.Model):
    event_tour_program = models.ForeignKey(EventTourProgram, on_delete=models.CASCADE,
                                           related_name='tour_program_gallery')
    image = models.ImageField(verbose_name='Фото', )

    class Meta:
        verbose_name = 'Фото дня программы тура'
        verbose_name_plural = 'Фото дней программы тура'


class EventPriceIncluded(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='price_included', verbose_name='Тур')
    title = models.CharField(max_length=200, verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Включено в цену'
        verbose_name_plural = 'Условия (Включено в цену)'


class EventPriceNotIncluded(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='price_not_included', verbose_name='Тур')
    title = models.CharField(max_length=200, verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Не включено в цену'
        verbose_name_plural = 'Условия (Не включено в цену)'
