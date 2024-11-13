from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from nested_inline import admin as nested_admin

from . import models


class HotelGalleryInline(nested_admin.NestedStackedInline):
    model = models.HotelGallery
    extra = 1


class HotelRoomImageInline(nested_admin.NestedTabularInline):
    model = models.HotelRoomImages
    extra = 1


class HotelRoomFacilityInline(nested_admin.NestedStackedInline, TranslationStackedInline):
    model = models.HotelRoomFacilities
    extra = 1


class HotelRoomInline(nested_admin.NestedStackedInline, TranslationStackedInline):
    fields = ['name', 'description', 'price']
    model = models.HotelRoom
    extra = 1
    inlines = [HotelRoomImageInline, HotelRoomFacilityInline]


@admin.register(models.Hotel)
class HotelAdmin(nested_admin.NestedModelAdmin, TranslationAdmin):
    list_display = ['id', 'name', 'stars', 'event', 'allocation_type']
    list_display_links = ['id', 'name']
    list_filter = ['event', 'allocation_type']
    list_editable = ['event', 'allocation_type']
    inlines = [
        HotelGalleryInline,
        HotelRoomInline,
    ]
