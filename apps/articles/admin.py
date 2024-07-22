from django.contrib import admin
from .models import Article, ArticleTextItem, ArticleImageItem, ArticleTopParagraphs, ArticleDecoratedTextItem


class ArticleTextItemInline(admin.TabularInline):
    model = ArticleTextItem
    extra = 1


class ArticleImageItemInline(admin.TabularInline):
    model = ArticleImageItem
    extra = 1


class ArticleTopParagraphsInline(admin.TabularInline):
    model = ArticleTopParagraphs
    extra = 1


class ArticleDecoratedTextItemInline(admin.TabularInline):
    model = ArticleDecoratedTextItem
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ArticleTopParagraphsInline,
        ArticleTextItemInline,
        ArticleDecoratedTextItemInline,
        ArticleImageItemInline,
    ]
