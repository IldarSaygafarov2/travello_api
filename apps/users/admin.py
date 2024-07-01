from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from .models import User


class CustomUserAdmin(UserAdmin):
	fieldsets = (
		(None, {"fields": ("username", "password", "verification_code", "is_verified")}),
		(_("Personal info"), {"fields": ("first_name", "last_name", "surname", "phone_number", "gender", "birth_date", "email")}),
		(
			_("Permissions"),
			{
				"fields": (
					"is_active",
					"is_staff",
					"is_superuser",
					"groups",
					"user_permissions",
				),
			},
		),
		(_("Important dates"), {"fields": ("last_login", "date_joined")}),
	)


admin.site.site_title = 'Travella Admin'
admin.site.site_header = 'Travella Administration'
admin.site.index_title = "Site administration"


admin.site.register(User, CustomUserAdmin)