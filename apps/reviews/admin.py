from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'user_type']
    list_display_links = ['id', 'fullname']
    list_filter = ['user_type']
