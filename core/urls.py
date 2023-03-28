from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)

urlpatterns_api = [
    path('', include('apps.shortener.urls_api'), name='main_shortener')
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    # my api
    path('api/v1/', include(urlpatterns_api)),

    # urls drf_spectacular
    path('schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('__debug__/', include('debug_toolbar.urls')), ]

# -------------------------------- Config Static and Media File -----------------------------------
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
