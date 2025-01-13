from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from nested_inline.admin import (
    NestedTabularInline,
    NestedModelAdmin,
    NestedStackedInline,
)

from . import models


class EventGalleryInline(NestedTabularInline):
    model = models.EventGallery
    extra = 1


class EventTourProgramGalleryInline(NestedStackedInline):
    model = models.EventTourProgramGallery
    extra = 1


class EventPriceIncludedInline(NestedStackedInline, TranslationStackedInline):
    model = models.EventPriceIncluded
    extra = 1


class EventImportantOptionInline(NestedStackedInline, TranslationStackedInline):
    model = models.EventImportantOption
    extra = 1


class EventPriceNotIncludedInline(NestedStackedInline, TranslationStackedInline):
    model = models.EventPriceNotIncluded
    extra = 1


class EventTourProgramAdmin(NestedStackedInline, TranslationStackedInline):
    fields = ["day", "title", "description"]
    model = models.EventTourProgram
    inlines = [EventTourProgramGalleryInline]
    extra = 1


class EventAdmin(NestedModelAdmin, TranslationAdmin):
    list_display = [
        "pk",
        "title",
        "price",
        "corporate_client_price",
        "country",
        "event_start",
        "event_end",
        "event_type",
    ]
    list_display_links = ["pk", "title"]
    list_editable = [
        "price",
        "event_type",
        "event_start",
        "event_end",
    ]
    list_filter = ["event_type"]
    inlines = [
        EventGalleryInline,
        EventTourProgramAdmin,
        EventPriceIncludedInline,
        EventPriceNotIncludedInline,
        EventImportantOptionInline,
    ]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(models.Event, EventAdmin)
