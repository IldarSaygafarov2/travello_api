from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}