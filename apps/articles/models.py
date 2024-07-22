from django.db import models


class Article(models.Model):
    title = models.CharField(verbose_name='Название статьи', max_length=100, unique=True)
    short_description = models.CharField(verbose_name='Краткое описание', max_length=100)
    preview_img = models.ImageField(verbose_name='Заставка', upload_to='images/articles/')
    preview_text = models.CharField(verbose_name='Слоган', max_length=100, null=True, blank=True)
    quote = models.CharField(verbose_name='Цитата', null=True, blank=True, max_length=100)
    published_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class ArticleTopParagraphs(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='top_paragraphs')
    text = models.TextField(verbose_name='Параграф')


class ArticleTextItem(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='text_items')
    text = models.TextField(verbose_name='Текст')


class ArticleDecoratedTextItem(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='decorated_text_items')
    text = models.TextField(verbose_name='Текст')


class ArticleImageItem(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='image_items')
    image = models.ImageField(verbose_name='Фото', upload_to='images/articles/', null=True, blank=True)
    descr = models.TextField(verbose_name='Описание под фото', null=True, blank=True)