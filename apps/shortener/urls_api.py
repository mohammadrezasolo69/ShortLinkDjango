from django.urls import path, include

app_name = 'shortener'
urlpatterns = [
    path('', include('apps.shortener.api.router'))
]
