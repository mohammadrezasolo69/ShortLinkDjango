from rest_framework import serializers

from apps.shortener.models import Shortener


class ShortenerBaseSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(source='get_short_url')

    class Meta:
        model = Shortener
        fields = (
            'id', 'long_url', 'short_url', 'status'
        )
