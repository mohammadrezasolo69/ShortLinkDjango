from rest_framework import serializers
from apps.statistic.models import Statistic


class StatisticListSerializer(serializers.ModelSerializer):
    time_click = serializers.CharField(source='get_time_click')

    class Meta:
        model = Statistic
        fields = (
            'ip', 'os', 'browser','language', 'time_click'
        )
