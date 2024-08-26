from django.contrib import admin
from nested_inline.admin import NestedModelAdmin

from . import models


class EventBookingAdmin(NestedModelAdmin):
    list_display = ['id', 'event', 'user', 'total_adult', 'total_children', 'event_type']
    list_filter = ['user', 'event_type', 'user']


admin.site.register(models.EventBooking, EventBookingAdmin)
