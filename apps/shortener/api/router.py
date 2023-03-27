from rest_framework import routers
from apps.shortener.api import viewset

router = routers.DefaultRouter()
router.register('shortener', viewset.ShortenerViewSet, basename='shortener')
urlpatterns = router.urls
