from modeltranslation.translator import TranslationOptions, translator

from .models import ServiceWorkingStep, Tag


class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


class ServiceWorkingStepTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


translator.register(ServiceWorkingStep, ServiceWorkingStepTranslationOptions)
translator.register(Tag, TagTranslationOptions)
