from django.urls import path, include

app_name = 'statistic'
urlpatterns = [
    path('statustic/', include('apps.statistic.api.router'))
]
