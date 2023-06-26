from django import test
from django.urls import reverse, resolve
from apps.shortener.api import viewset


class CategoryRouterTestCase(test.SimpleTestCase):
    def test_app_name(self):
        path = '/api/v1/shortener/'
        self.assertTrue(resolve(path).app_name)
        self.assertEqual(resolve(path).app_name, 'shortener')

    def test_router_list_create(self):
        path = reverse('shortener:category-list')
        self.assertEqual(resolve(path).func.__name__, viewset.CategoryViewSet.__name__)

    def test_router_update_delete_retrieve(self):
        path = reverse('shortener:category-detail',kwargs={'pk':1})
        self.assertEqual(resolve(path).func.__name__, viewset.CategoryViewSet.__name__)
