from django.contrib import admin
from . import models
from nested_inline.admin import NestedTabularInline, NestedModelAdmin


class EventGalleryInline(NestedTabularInline):
    model = models.EventGallery
    extra = 1


class EventTourProgramGalleryInline(NestedTabularInline):
    model = models.EventTourProgramGallery
    extra = 1


class EventPriceIncludedInline(NestedTabularInline):
    model = models.EventPriceIncluded
    extra = 1


class EventPriceNotIncludedInline(NestedTabularInline):
    model = models.EventPriceNotIncluded
    extra = 1


class EventTourProgramAdmin(NestedTabularInline):
    fields = ['day', 'title', 'description']
    model = models.EventTourProgram
    inlines = [EventTourProgramGalleryInline]
    extra = 1


class EventAdmin(NestedModelAdmin):
    inlines = [
        EventGalleryInline,
        EventTourProgramAdmin,
        EventPriceIncludedInline,
        EventPriceNotIncludedInline,
    ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Event, EventAdmin)
