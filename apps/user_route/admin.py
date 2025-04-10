from django.contrib import admin
from apps.users.models import Tourist

from .models import (
    UserTourRoute,
    UserTourHotel,
    UserTourTransport,
    UserRouteGuide,
    UserRouteAdditionalService,
)


class UserRouteTouristInline(admin.TabularInline):
    model = Tourist
    extra = 1
    # fk_name = "user"


class UserTourHotelInline(admin.TabularInline):
    model = UserTourHotel
    extra = 1


class UserTourTransportInline(admin.TabularInline):
    model = UserTourTransport
    extra = 1


class UserRouteGuideInline(admin.TabularInline):
    model = UserRouteGuide
    extra = 1


class UserRouteAdditionalServiceInline(admin.TabularInline):
    model = UserRouteAdditionalService
    extra = 1


@admin.register(UserTourRoute)
class UserTourRouteAdmin(admin.ModelAdmin):
    inlines = [
        UserTourHotelInline,
        UserTourTransportInline,
        UserRouteGuideInline,
        UserRouteAdditionalServiceInline,
        # UserRouteTouristInline,
    ]
