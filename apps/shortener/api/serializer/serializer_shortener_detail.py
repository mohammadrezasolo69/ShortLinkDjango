from rest_framework import serializers

from apps.shortener.models import Shortener
from apps.shortener.api.serializer import CategoryBaseSerializer



class ShortenerDetailSerializer(serializers.ModelSerializer):
    short_url = serializers.URLField(source='get_short_url')
    expired_at = serializers.CharField(source='set_expired_at')
    category = CategoryBaseSerializer(required=False)
    # TODO:add Statistics

    class Meta:
        model = Shortener
        fields = (
            'id', 'user', 'category', 'long_url', 'short_url', 'expired_at','set_QR_code', 'set_password','status'
        )
        read_only_fields = (
            'id','user', 'category', 'long_url', 'short_url', 'expired_at', 'set_password','set_QR_code'
        )
