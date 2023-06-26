from django.contrib import admin

from apps.statistic.models import Statistic


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('ip', 'shortener', 'os', 'browser', 'get_time_click')
    list_filter = ('shortener', 'os', 'browser')
    search_fields = ('ip', 'shortener', 'os', 'browser')
