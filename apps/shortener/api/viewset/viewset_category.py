from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, permissions

from apps.shortener.models import Category
from apps.shortener import permissions as custom_permissions
from apps.shortener.api.serializer import (
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategoryCreateUpdateSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.IsAuthenticated, custom_permissions.IsUser]

    def get_queryset(self):
        return self.model.objects.select_related(
            'user').filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        elif self.action in ['create', 'update', 'partial']:
            return CategoryCreateUpdateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    @method_decorator(cache_page(60), name='retrieve')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
