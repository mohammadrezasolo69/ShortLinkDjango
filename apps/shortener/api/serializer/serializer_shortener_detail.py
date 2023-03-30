from rest_framework import serializers

from apps.shortener.models import Shortener
from apps.shortener.api.serializer import CategoryBaseSerializer
from apps.statistic.api.serializer import StatisticBaseSerializer


class ShortenerDetailSerializer(serializers.ModelSerializer):
    short_url = serializers.URLField(source='get_short_url')
    expired_at = serializers.CharField(source='set_expired_at')
    category = CategoryBaseSerializer(required=False)
    statistics = StatisticBaseSerializer(many=True)

    class Meta:
        model = Shortener
        fields = (
            'id', 'user', 'category', 'long_url', 'short_url', 'expired_at', 'set_QR_code', 'set_password', 'status',
            'statistics'
        )
        read_only_fields = (
            'id', 'user', 'category', 'long_url', 'short_url', 'expired_at', 'set_password', 'set_QR_code'
        )
