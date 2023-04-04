from django.urls import path
from apps.statistic.api import viewset

urlpatterns = [
    path('<str:code>/', viewset.StatisticListView.as_view(), name='statistic_list')
]
