from rest_framework import viewsets

from apps.shortener.models import Shortener
from apps.shortener.api.serializer import ShortenerListSerializer,ShortenerDetailSerializer


class ShortenerViewSet(viewsets.ModelViewSet):
    model = Shortener
    serializer_class = ShortenerDetailSerializer

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortenerListSerializer
        return self.serializer_class