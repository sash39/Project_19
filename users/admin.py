from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_active']
    list_registration = ['id', 'email', 'password', 'confirm_password', ]

admin.site.unregister(User)