from modeltranslation.translator import TranslationOptions, translator
from . import models


class EventTourProgramTranslationOptions(TranslationOptions):
    fields = ("title", "description")


class EventPriceIncludedTranslationOptions(TranslationOptions):
    fields = ("title",)


class EventPriceNotIncludedTranslationOptions(TranslationOptions):
    fields = ("title",)


class EventImportantOptionTranslationOptions(TranslationOptions):
    fields = ("title",)


class EventTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "short_description",
        "full_description",
        "country_from",
        "country",
        "gathering_place",
    )


translator.register(models.Event, EventTranslationOptions)
translator.register(models.EventPriceIncluded, EventPriceIncludedTranslationOptions)
translator.register(models.EventImportantOption, EventImportantOptionTranslationOptions)
translator.register(
    models.EventPriceNotIncluded,
    EventPriceNotIncludedTranslationOptions,
)
translator.register(models.EventTourProgram, EventTourProgramTranslationOptions)
