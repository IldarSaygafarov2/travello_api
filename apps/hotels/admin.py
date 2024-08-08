from django.contrib import admin
from nested_inline import admin as nested_admin

from . import models


class HotelGalleryInline(nested_admin.NestedTabularInline):
    model = models.HotelGallery
    extra = 1


class HotelFacilityInline(nested_admin.NestedTabularInline):
    model = models.HotelFacility
    extra = 1


class HotelEntertainmentInline(nested_admin.NestedTabularInline):
    model = models.HotelEntertainment
    extra = 1


class HotelRoomImageInline(nested_admin.NestedTabularInline):
    model = models.HotelRoomImages
    extra = 1


class HotelRoomFacilityInline(nested_admin.NestedTabularInline):
    model = models.HotelRoomFacilities
    extra = 1


class HotelRoomInline(nested_admin.NestedStackedInline):
    fields = ['name', 'is_all_inclusive', 'description', 'nights', 'price', 'until']
    model = models.HotelRoom
    extra = 1
    inlines = [HotelRoomImageInline, HotelRoomFacilityInline]


@admin.register(models.Hotel)
class HotelAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        HotelGalleryInline,
        HotelFacilityInline,
        HotelEntertainmentInline,
        HotelRoomInline,
    ]
