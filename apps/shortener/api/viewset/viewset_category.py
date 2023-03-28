from rest_framework import viewsets

from apps.shortener.models import Category
from apps.shortener.api.serializer import (
    CategoryListSerializer,
    CategoryDetailSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return self.model.objects.select_related(
            'user').filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        return self.serializer_class