import base64
from rest_framework import test, status
from django.urls import reverse
from django.contrib.auth import get_user_model

from apps.shortener.models import Shortener
from apps.shortener.api.serializer import (
    ShortenerCreateUpdateSerializer,
    ShortenerListSerializer,
    ShortenerDetailSerializer
)


class ShortenerViewSetTestCase(test.APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='admin@gmail.com'
        )
        self.user.set_password('admin')
        self.user.save()

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode('admin@gmail.com:admin'.encode()).decode()
        }

        self.shortener = Shortener.objects.create(
            user=self.user,
            long_url='https://google.com',
            short='my_short'
        )

    def test_list(self):
        path = reverse('shortener:shortener-list')
        response = self.client.get(path, **self.auth_headers)

        shortener = Shortener.objects.all()
        serializer = ShortenerListSerializer(shortener, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_no_permission(self):
        path = reverse('shortener:shortener-list')
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve(self):
        path = reverse('shortener:shortener-detail',kwargs={'pk':1})
        response = self.client.get(path, **self.auth_headers)

        shortener = Shortener.objects.get(pk=1)
        serializer = ShortenerDetailSerializer(shortener)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_no_permission(self):
        path = reverse('shortener:shortener-detail',kwargs={'pk':1})
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

