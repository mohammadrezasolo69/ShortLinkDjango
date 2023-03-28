from rest_framework import serializers

from apps.shortener.models import Shortener
from apps.shortener.api.serializer import CategoryBaseSerializer


class ShortenerCreateUpdateSerializer(serializers.ModelSerializer):
    category = CategoryBaseSerializer()

    class Meta:
        model = Shortener
        exclude = ('QR_code', 'status')
        read_only_fields = ('user', 'created_at', 'updated_at')
