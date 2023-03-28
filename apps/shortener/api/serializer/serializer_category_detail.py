from rest_framework import serializers

from apps.shortener.models import Category
from apps.shortener.api.serializer import ShortenerBaseSerializer


class CategoryDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField(source='get_created_at')
    links = serializers.SerializerMethodField(method_name='get_links')

    class Meta:
        model = Category
        fields = (
            'id', 'created_at', 'title', 'slug', 'color', 'user', 'status', 'links'
        )
        read_only_fields = (
            'id', 'created_at', 'title', 'slug', 'color', 'user', 'status', 'links'
        )

    def get_links(self, obj):
        queryset = obj.shortener.filter(user=obj.user)
        return ShortenerBaseSerializer(queryset, many=True).data
