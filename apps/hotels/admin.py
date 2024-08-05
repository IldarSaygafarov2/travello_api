from django.contrib import admin

from . import models


class HotelGalleryInline(admin.TabularInline):
    model = models.HotelGallery
    extra = 1


class HotelFacilityInline(admin.TabularInline):
    model = models.HotelFacility
    extra = 1


class HotelEntertainmentInline(admin.TabularInline):
    model = models.HotelEntertainment
    extra = 1


@admin.register(models.Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = [
        HotelGalleryInline,
        HotelFacilityInline,
        HotelEntertainmentInline,
    ]

