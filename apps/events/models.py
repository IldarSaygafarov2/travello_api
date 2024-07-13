from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

slugify


class EventType(models.TextChoices):
    WORLD = 'Мировой'
    LOCAL = 'По узбекистану'

    __empty__ = '-'


def event_images_upload_to(instance, filename):
    return f'images/events/{instance.slug}/{filename}'


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название ивента')
    slug = models.SlugField(verbose_name='Слаг',
                            help_text='Данное поле заполнять не нужно, оно заполняется автоматически', blank=True)
    short_description = models.TextField(verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name='Полное описание')
    preview = models.ImageField(verbose_name='Фото', upload_to=event_images_upload_to, blank=True)
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    country = models.CharField(verbose_name='Страна ивента')
    event_start = models.SmallIntegerField(verbose_name='Число начала ивента')
    event_end = models.SmallIntegerField(verbose_name='Число конца ивента')
    days = models.SmallIntegerField(verbose_name='Количество дней тура')
    nights = models.SmallIntegerField(verbose_name='Количество ночей тура')
    gathering_place = models.CharField(verbose_name='Место сбора группы')
    minimum_age = models.IntegerField(verbose_name='Минимальный возраст')
    people_in_group = models.IntegerField(verbose_name='Количество человек в группе')
    event_type = models.CharField(verbose_name='Тип тура', max_length=20, choices=EventType.choices,
                                  default=EventType.WORLD)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ивент'
        verbose_name_plural = 'Ивенты'


def event_images_gallery_upload_to(instance, filename):
    return f'images/events/{instance.slug}/gallery/{filename}'


class EventGallery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Ивент', related_name='images_gallery')
    image = models.ImageField(verbose_name='Фото', upload_to=event_images_gallery_upload_to, null=True, blank=True)


# title
# day
# description
# event_id

class EventTourProgram(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    slug = models.SlugField(verbose_name='Слаг')
    day = models.IntegerField(verbose_name='День', help_text='День тура, например: "1 день, 2 день"')
    description = RichTextField(verbose_name='Описание')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tour_program')

    def __str__(self):
        return self.title


# def event_images_gallery_upload_to(instance, filename):
#     return f'images/events/{instance.slug}/gallery/{filename}'


class EventTourProgramGallery(models.Model):
    event_tour_program = models.ForeignKey(EventTourProgram, on_delete=models.CASCADE,
                                           related_name='tour_program_gallery')
    image = models.ImageField(verbose_name='Фото', )


# event_id
# title
class EventPriceIncluded(models.Model):
    pass


# event_id
# title
class EventPriceNotIncluded(models.Model):
    pass
