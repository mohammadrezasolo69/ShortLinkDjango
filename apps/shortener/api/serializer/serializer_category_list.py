from rest_framework import serializers

from apps.shortener.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    created_at = serializers.CharField(source='get_created_at')
    count_link = serializers.SerializerMethodField(method_name='get_count_link')

    class Meta:
        model = Category
        fields = (
            'id', 'created_at', 'title', 'slug', 'color', 'user', 'status', 'count_link'
        )
        read_only_fields = (
            'id', 'created_at', 'title', 'slug', 'color', 'user', 'status','count_link'
        )

    def get_count_link(self, obj):
        return obj.shortener.count()
