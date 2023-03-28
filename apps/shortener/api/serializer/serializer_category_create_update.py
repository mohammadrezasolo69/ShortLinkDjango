from rest_framework import serializers

from apps.shortener.models import Category


class CategoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'created_at', 'title', 'slug', 'color', 'user', 'status'
        )
        read_only_fields = (
            'id', 'created_at', 'user', 'status',
        )
