from django.contrib import admin
from .models import CorporateClientRequest


class CorporateClientRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number', 'client_type', 'created_at']
    list_display_links = ['id', 'name']


admin.site.register(CorporateClientRequest, CorporateClientRequestAdmin)
