from django.contrib.auth import get_user_model
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


@admin.register(get_user_model())
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'get_full_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('id', 'email', 'get_full_name')
    ordering = ('id',)

    fieldsets = (
        (_('Main'), {'fields': ('email', 'first_name', 'last_name')}),
        (_('Permission'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Data'), {'fields': ('date_joined',)}),
    )
