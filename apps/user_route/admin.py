from django.contrib import admin

from .models import (
    UserTourRoute,
)


@admin.register(UserTourRoute)
class UserTourRouteAdmin(admin.ModelAdmin):
    pass
