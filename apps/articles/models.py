from django.db import models


class Article(models.Model):
    title = models.CharField(verbose_name='Название статьи', max_length=100, unique=True)
    short_description = models.CharField(verbose_name='Краткое описание', max_length=100)
    preview_img = models.ImageField(verbose_name='Заставка', upload_to='images/articles/')
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'