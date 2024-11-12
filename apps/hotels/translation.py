from modeltranslation.translator import TranslationOptions, translator

from . import models


class HotelsTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'country',
        'address',
        'full_description',
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
translator.register(models.HotelRoom, HotelRoomTranslationOptions)
translator.register(models.HotelRoomFacilities, HotelRoomFacilitiesTranslationOptions)
