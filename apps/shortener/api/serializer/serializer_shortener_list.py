from rest_framework import serializers

from apps.shortener.models import Shortener


class ShortenerListSerializer(serializers.ModelSerializer):
    short_url = serializers.URLField(source='get_short_url')
    created_at = serializers.CharField(source='get_created_at')
    expired_at = serializers.CharField(source='set_expired_at')

    # TODO:count click in link

    class Meta:
        model = Shortener
        fields = (
            'id', 'category', 'long_url', 'short_url','expired_at', 'created_at', 'user', 'status'
        )
        read_only_fields = (
            'id', 'category', 'long_url', 'short_url', 'created_at', 'user', 'status'
        )
