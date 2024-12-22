from django.contrib import admin

from . import models


class GuideLangInline(admin.TabularInline):
    model = models.GuideLanguage
    extra = 1


@admin.register(models.Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ["pk", "user_id"]
    inlines = [GuideLangInline]


class GuideTourExpectationInline(admin.TabularInline):
    model = models.GuideTourExpectation
    extra = 1


class GuideTourOrganizationalDetailInline(admin.TabularInline):
    model = models.GuideTourOrganizationalDetail
    extra = 1


class GuideScheduleInline(admin.TabularInline):
    model = models.GuideSchedule
    extra = 1


class GuideTourPhotoInline(admin.TabularInline):
    model = models.GuideTourPhoto
    extra = 1


@admin.register(models.GuideTour)
class GuideTourAdmin(admin.ModelAdmin):

    inlines = [
        GuideTourExpectationInline,
        GuideTourOrganizationalDetailInline,
        GuideScheduleInline,
        GuideTourPhotoInline,
    ]
