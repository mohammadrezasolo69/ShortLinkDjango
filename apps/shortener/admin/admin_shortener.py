from django.contrib import admin

from apps.shortener.models import Shortener


@admin.register(Shortener)
class ShortenerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'get_short_url', 'long_url', 'user', 'set_expired_at', 'set_QR_code', 'set_password', 'category')
    list_filter = ('status',)
    search_fields = ('id', 'short', 'user', 'category')
