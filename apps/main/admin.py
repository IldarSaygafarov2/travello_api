from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


class TagAdmin(TranslationAdmin):
    list_display = ('name', )


class ServiceWorkingStepAdmin(TranslationAdmin):
    pass


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class StaticMediaContentItemInline(admin.StackedInline):
    model = models.StaticMediaContentItem
    extra = 1


class StaticMediaContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'page', 'page_slug']
    list_display_links = ['id', 'page']
    prepopulated_fields = {'page_slug': ('page',)}
    inlines = [StaticMediaContentItemInline]


admin.site.register(models.Newsletter, NewsLetterAdmin)
admin.site.register(models.StaticMediaContent, StaticMediaContentAdmin)
admin.site.register(models.ServiceWorkingStep, ServiceWorkingStepAdmin)
admin.site.register(models.Tag, TagAdmin)