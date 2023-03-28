from rest_framework import serializers

from apps.shortener.models import Shortener


class ShortenerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        exclude = ('QR_code', 'status')
        read_only_fields = ('user', 'created_at', 'updated_at')
