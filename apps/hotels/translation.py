from modeltranslation.translator import TranslationOptions, translator
from . import models


class HotelsTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'country',
        'address',
        'short_description',
        'full_description',
    )


class HotelFacilitiesTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


class HotelEntertainmentTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


class HotelRoomTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'description'
    )


class HotelRoomFacilitiesTranslationOptions(TranslationOptions):
    fields = (
        'facility',
    )


translator.register(models.Hotel, HotelsTranslationOptions)
translator.register(models.HotelFacility, HotelFacilitiesTranslationOptions)
translator.register(models.HotelEntertainment, HotelEntertainmentTranslationOptions)
translator.register(models.HotelRoom, HotelRoomTranslationOptions)
translator.register(models.HotelRoomFacilities, HotelRoomFacilitiesTranslationOptions)
