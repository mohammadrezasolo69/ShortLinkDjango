from rest_framework import generics
from apps.statistic.models import Statistic
from apps.statistic.api.seriaizer import StatisticListSerializer


class StatisticListView(generics.ListAPIView):
    model = Statistic
    serializer_class = StatisticListSerializer

    def get_queryset(self):
        return self.model.objects.select_related(
            'shortener').filter(shortener__short=self.kwargs.get('code'))
