from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from . import models

import nested_admin


class HotelRoomSeasonPriceInline(nested_admin.NestedStackedInline):
    model = models.HotelPriceInSeason


class HotelRoomNotSeasonPriceInline(nested_admin.NestedStackedInline):
    model = models.HotelPriceInNotSeason


class HotelGalleryInline(nested_admin.NestedStackedInline):
    model = models.HotelGallery


class HotelRoomImageInline(nested_admin.NestedStackedInline):
    model = models.HotelRoomImages


class HotelRoomFacilityInline(
    TranslationStackedInline, nested_admin.NestedStackedInline
):
    model = models.HotelRoomFacilities


# @admin.register(models.HotelRoom)
class HotelRoomInline(nested_admin.NestedStackedInline):
    model = models.HotelRoom
    inlines = [
        HotelRoomImageInline,
        HotelRoomFacilityInline,
        HotelRoomSeasonPriceInline,
        HotelRoomNotSeasonPriceInline,
    ]


@admin.register(models.Hotel)
class HotelAdmin(TranslationAdmin, nested_admin.NestedModelAdmin):
    model = models.Hotel
    list_display = [
        "id",
        "name",
        "minimum_price",
        "stars",
        "allocation_type",
    ]
    list_display_links = ["id", "name"]
    # list_filter = ["event", "allocation_type"]
    list_filter = ["allocation_type", "hotel_type", "stars", "city"]
    # list_editable = ["event", "allocation_type"]
    list_editable = ["allocation_type"]
    search_fields = ["name"]
    inlines = [HotelGalleryInline, HotelRoomInline]
