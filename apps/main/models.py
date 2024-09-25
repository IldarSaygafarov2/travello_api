from django.db import models


class Newsletter(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя отправителя')
    email = models.EmailField(verbose_name='Почта отправителя')
    text = models.TextField(verbose_name='Сообщение')
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        verbose_name = 'Вопрос пользователя'
        verbose_name_plural = 'Вопросы пользователя'


class StaticMediaContent(models.Model):
    page = models.CharField(verbose_name='Название страницы', max_length=100, unique=True)
    page_slug = models.SlugField(verbose_name='Слаг страницы', help_text='Данное поле заполнять вручную не нужно')

    def __str__(self):
        return f'{self.page}: {self.page_slug}'

    class Meta:
        verbose_name = 'Статичный медиа контент'
        verbose_name_plural = 'Статичный медиа контент'


def static_media_content_file_path(instance, filename):
    return f'main/media_content/{instance.static_media.page_slug}/{filename}'


class StaticMediaContentItem(models.Model):
    static_media = models.ForeignKey(StaticMediaContent, on_delete=models.CASCADE, related_name='media_content')
    media = models.FileField(verbose_name='Медиа контент для страницы', upload_to=static_media_content_file_path,
                             null=True, blank=True)


class ServiceWorkingStep(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    subtitle = models.CharField(verbose_name='Подзаголовок', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Работа сервиса'
        verbose_name_plural = 'Работа сервиса'


class Tag(models.Model):
    name = models.CharField(verbose_name='название', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
