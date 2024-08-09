from django.contrib import admin
from .models import Article, ArticleTextItem, ArticleImageItem, ArticleTopParagraphs, ArticleDecoratedTextItem
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

class ArticleTextItemInline(TranslationStackedInline):
    model = ArticleTextItem
    extra = 1


class ArticleImageItemInline(TranslationStackedInline):
    model = ArticleImageItem
    extra = 1


class ArticleTopParagraphsInline(TranslationStackedInline):
    model = ArticleTopParagraphs
    extra = 1


class ArticleDecoratedTextItemInline(TranslationStackedInline):
    model = ArticleDecoratedTextItem
    extra = 1


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'published_at']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ArticleTopParagraphsInline,
        ArticleTextItemInline,
        ArticleDecoratedTextItemInline,
        ArticleImageItemInline,
    ]
