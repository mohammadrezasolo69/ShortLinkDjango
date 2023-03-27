from rest_framework import serializers

from apps.shortener.models import Shortener


class ShortenerListSerializer(serializers.ModelSerializer):
    short_url = serializers.URLField(source='get_short_url')
    expired_at = serializers.CharField(source='expired_at_active')
    
    class Meta:
        model = Shortener
        fields = (
            'id', 'category', 'long_url', 'short_url', 'expired_at', 'password_active'
        )
        read_only_fields = (
            'id', 'category', 'long_url', 'short_url', 'expired_at', 'password_active'
        )
