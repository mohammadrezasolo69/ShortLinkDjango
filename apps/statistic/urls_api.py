from django.urls import path, include

app_name = 'statistic'
urlpatterns = [
    path('statistic/', include('apps.statistic.api.router'))
]
