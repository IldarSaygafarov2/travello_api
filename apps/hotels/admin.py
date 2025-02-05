from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from nested_inline import admin as nested_inline_admin
from . import models


class HotelGalleryInline(admin.TabularInline):
    model = models.HotelGallery
    extra = 1


class HotelRoomImageInline(nested_inline_admin.NestedStackedInline):
    model = models.HotelRoomImages
    extra = 1


class HotelRoomFacilityInline(TranslationStackedInline, nested_inline_admin.NestedStackedInline):
    model = models.HotelRoomFacilities
    extra = 1


# @admin.register(models.HotelRoom)
class HotelRoomInline(nested_inline_admin.NestedStackedInline):
    model = models.HotelRoom
    extra = 1
    inlines = [HotelRoomImageInline, HotelRoomFacilityInline]


@admin.register(models.Hotel)
class HotelAdmin(TranslationAdmin, nested_inline_admin.NestedModelAdmin):
    list_display = [
        "id",
        "name",
        "averrage_price",
        "minimum_price",
        "stars",
        "allocation_type",
    ]
    list_display_links = ["id", "name"]
    # list_filter = ["event", "allocation_type"]
    list_filter = ["allocation_type"]
    # list_editable = ["event", "allocation_type"]
    list_editable = ["allocation_type"]
    inlines = [HotelGalleryInline, HotelRoomInline]
