from django.contrib import admin

from .models import Guide, GuideLanguage


class GuideLangInline(admin.TabularInline):
    model = GuideLanguage
    extra = 1


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    inlines = [GuideLangInline]


