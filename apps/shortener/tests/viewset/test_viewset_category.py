import base64
import json

from rest_framework import test, status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from apps.shortener.models import Category
from apps.shortener.api.serializer import (
    CategoryDetailSerializer,
    CategoryListSerializer,
    CategoryCreateUpdateSerializer
)


class CategoryViewSetTestCase(test.APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='admin@gmail.com'
        )

        self.refresh_for_user = RefreshToken.for_user(self.user)

        self.shortener = Category.objects.create(
            user=self.user,
            title='title one'
        )

        self.valid_data = {
            "user": self.user,
            "title": 'title two'
        }

        self.no_valid_data = {
            "user": '',
            "title": ''
        }

        self.update_valid_date = {
            "user": self.user,
            "title": 'title two update'
        }

        self.no_update_valid_date = {
            "user": '',
            "title": ''
        }

    # --------------------------------- List --------------------------------------
    def test_list(self):
        path = reverse('shortener:category-list')
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh_for_user.access_token}"
        )
        response = self.client.get(path=path)
        shortener = Category.objects.all()
        serializer = CategoryListSerializer(shortener, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_no_permission(self):
        path = reverse('shortener:category-list')
        response = self.client.get(path=path)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    #--------------------------------- Create --------------------------------------

    def test_create(self):
        path = reverse('shortener:category-list')
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh_for_user.access_token}"
        )
        response = self.client.post(path=path, data=self.valid_data)
        content = json.loads(response.content)

        serializer = CategoryCreateUpdateSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(content.get('user'))
        self.assertTrue(content.get('status'))
        self.assertTrue(content.get('slug'))
        self.assertTrue(content.get('color'))
        self.assertTrue(content.get('created_at'))

        self.assertEqual(content.get('title'), serializer.data.get('title'))

    def test_create_no_valid_data(self):
        path = reverse('shortener:category-list')
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh_for_user.access_token}"
        )
        response = self.client.post(path=path, data=self.no_valid_data)

        serializer = CategoryCreateUpdateSerializer(data=self.no_valid_data)
        serializer.is_valid(raise_exception=False)

        print(serializer.data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEquals(response.status_code, status.HTTP_201_CREATED)

    def test_create_no_permission(self):
        path = reverse('shortener:category-list')
        response = self.client.post(path, self.valid_data)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotEquals(response.status_code, status.HTTP_201_CREATED)

    # --------------------------------- Update --------------------------------------

    def test_update(self):
        path = reverse('shortener:category-detail', kwargs={'pk': 1})
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh_for_user.access_token}"
        )
        response = self.client.put(path=path, data=self.update_valid_date)
        content = json.loads(response.content)

        serializer = CategoryCreateUpdateSerializer(data=self.update_valid_date)
        serializer.is_valid(raise_exception=True)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertTrue(content.get('user'))
        self.assertTrue(content.get('status'))
        self.assertTrue(content.get('slug'))
        self.assertTrue(content.get('color'))
        self.assertTrue(content.get('created_at'))

        self.assertEqual(content.get('title'), serializer.data.get('title'))

    def test_update_no_valid_data(self):
        path = reverse('shortener:category-detail', kwargs={'pk': 1})
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh_for_user.access_token}"
        )
        response = self.client.put(path=path, data=self.no_update_valid_date)

        serializer = CategoryCreateUpdateSerializer(data=self.no_update_valid_date)
        serializer.is_valid(raise_exception=False)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEquals(response.status_code, status.HTTP_201_CREATED)

    def test_update_no_permission(self):
        path = reverse('shortener:category-detail', kwargs={'pk': 1})
        response = self.client.put(path=path, data=self.update_valid_date)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotEquals(response.status_code, status.HTTP_201_CREATED)
    #
    # --------------------------------- Retrieve --------------------------------------

    def test_retrieve(self):
        path = reverse('shortener:category-detail', kwargs={'pk': 1})
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh_for_user.access_token}"
        )
        response = self.client.get(path=path)

        shortener = Category.objects.get(pk=1)
        serializer = CategoryDetailSerializer(shortener)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_no_permission(self):
        path = reverse('shortener:category-detail', kwargs={'pk': 1})
        response = self.client.get(path=path)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # --------------------------------- Delete --------------------------------------

    def test_delete(self):
        path = reverse('shortener:category-detail', kwargs={'pk': 1})
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {self.refresh_for_user.access_token}"
        )
        response = self.client.delete(path=path)

        shortener = Category.objects.all().count()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(shortener, 0)

    def test_delete_no_permission(self):
        path = reverse('shortener:category-detail', kwargs={'pk': 1})
        response = self.client.delete(path=path)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
