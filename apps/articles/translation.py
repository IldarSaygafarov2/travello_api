from modeltranslation.translator import TranslationOptions, translator

from . import models


class ArticleTopParagraphsTranslationOptions(TranslationOptions):
    fields = ('text',)


class ArticleTextItemTranslationOptions(TranslationOptions):
    fields = ('text',)


class ArticleDecoratedTextItemTranslationOptions(TranslationOptions):
    fields = ('text',)


class ArticleImageItemTranslationOptions(TranslationOptions):
    fields = ('descr',)


class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'preview_text', 'quote')


translator.register(models.Article, ArticleTranslationOptions)
translator.register(models.ArticleTopParagraphs, ArticleTopParagraphsTranslationOptions)
translator.register(models.ArticleTextItem, ArticleTextItemTranslationOptions)
translator.register(models.ArticleDecoratedTextItem, ArticleDecoratedTextItemTranslationOptions)
translator.register(models.ArticleImageItem, ArticleImageItemTranslationOptions)
