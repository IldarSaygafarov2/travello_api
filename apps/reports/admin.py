from django.contrib import admin
from . import models


class DailySalesAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'agent',
                    'supplier']
    list_editable = ['agent', 'supplier']
    list_filter = ['date', 'agent', 'supplier']


admin.site.register(models.Agent)
admin.site.register(models.Supplier)
admin.site.register(models.DailySales, DailySalesAdmin)
admin.site.register(models.AgentReport)
admin.site.register(models.SupplierReport)
