from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
	pass


admin.site.site_title = 'Travella Admin'
admin.site.site_header = 'Travella Administration'
admin.site.index_title = "Site administration"


admin.site.register(User, UserAdmin)