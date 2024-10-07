from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import CorporateClientRequest, OurClient


class CorporateClientRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number', 'client_type', 'created_at']
    list_display_links = ['id', 'name']


class OurClientAdmin(TranslationAdmin):
    pass


admin.site.register(CorporateClientRequest, CorporateClientRequestAdmin)
admin.site.register(OurClient, OurClientAdmin)
