from rest_framework import viewsets

from apps.shortener.models import Category
from apps.shortener.api.serializer import (
    CategoryListSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        return self.model.objects.select_related(
            'user').filter(user=self.request.user)
