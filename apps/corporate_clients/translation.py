from .models import OurClient
from modeltranslation.translator import translator, TranslationOptions


class OurClientTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(OurClient, OurClientTranslationOptions)