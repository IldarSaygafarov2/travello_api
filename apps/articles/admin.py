from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from .models import Article, ArticleTextItem, ArticleImageItem, ArticleTopParagraphs, ArticleDecoratedTextItem


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
    list_display = ['id', 'title', 'published_at', 'show_on_home_page']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['show_on_home_page']
    inlines = [
        ArticleTopParagraphsInline,
        ArticleTextItemInline,
        ArticleDecoratedTextItemInline,
        ArticleImageItemInline,
    ]
