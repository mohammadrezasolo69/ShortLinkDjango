from django.utils.decorators import method_decorator
from django.utils.functional import cached_property
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, permissions
from apps.shortener import permissions as custom_permissions
from apps.shortener.models import Shortener
from apps.shortener.api.serializer import (
    ShortenerListSerializer,
    ShortenerDetailSerializer,
    ShortenerCreateUpdateSerializer,
)


class ShortenerViewSet(viewsets.ModelViewSet):
    model = Shortener
    serializer_class = ShortenerDetailSerializer
    permission_classes = [permissions.IsAuthenticated, custom_permissions.IsUser]

    def get_queryset(self):
        return self.model.objects.select_related(
            'user','category').filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortenerListSerializer
        elif self.action in ['create', 'update', 'partial']:
            return ShortenerCreateUpdateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    @method_decorator(cache_page(60), name='retrieve')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
