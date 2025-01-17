from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from . import models


class HotelGalleryInline(admin.TabularInline):
    model = models.HotelGallery
    extra = 1


class HotelRoomImageInline(admin.TabularInline):
    model = models.HotelRoomImages
    extra = 1


class HotelRoomFacilityInline(TranslationStackedInline):
    model = models.HotelRoomFacilities
    extra = 1


@admin.register(models.HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ["pk", "name"]
    list_display_links = ["pk", "name"]
    inlines = [HotelRoomImageInline, HotelRoomFacilityInline]


@admin.register(models.Hotel)
class HotelAdmin(TranslationAdmin):
    list_display = [
        "id",
        "name",
        "averrage_price",
        "minimum_price",
        "stars",
        # "event",
        "allocation_type",
    ]
    list_display_links = ["id", "name"]
    # list_filter = ["event", "allocation_type"]
    list_filter = ["allocation_type"]
    # list_editable = ["event", "allocation_type"]
    list_editable = ["allocation_type"]
    inlines = [
        HotelGalleryInline,
    ]
