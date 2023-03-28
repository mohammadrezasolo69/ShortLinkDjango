from rest_framework import serializers

from apps.shortener.models import Category


class CategoryBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'title', 'slug', 'status'
        )
