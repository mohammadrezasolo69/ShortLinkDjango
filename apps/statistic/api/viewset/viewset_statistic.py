from rest_framework import generics, permissions
from apps.statistic.models import Statistic
from apps.statistic.api.serializer import StatisticListSerializer
from apps.utils import permissions as custom_permissions


class StatisticListView(generics.ListAPIView):
    model = Statistic
    serializer_class = StatisticListSerializer
    permission_classes = [permissions.IsAuthenticated, custom_permissions.IsUser]

    def get_queryset(self):
        return self.model.objects.select_related(
            'shortener').filter(shortener__short=self.kwargs.get('code'))
