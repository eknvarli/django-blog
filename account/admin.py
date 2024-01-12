from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUser

@admin.register(CustomUser)
class CustomAdmin(UserAdmin):
    list_display = ('username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Setting Area', {
            'fields': ['avatar']
        }),
    )