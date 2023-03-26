from django.contrib import admin

from apps.shortener.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'color', 'user', 'status')
    list_filter = ('status',)
    search_fields = ('id', 'title', 'slug', 'color', 'user')
