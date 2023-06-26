from django import test
from django.contrib.auth import get_user_model
from apps.shortener.models import Category


class CategoryModelTestCase(test.TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='admin@gmail.com',
            password='admin123123'
        )

        self.category = Category.objects.create(
            title='it one',
            color='#9842f5',
            user=self.user
        )

    def test_str_method(self):
        self.assertTrue(self.category)
        self.assertEqual(str(self.category), 'it one')
        self.assertNotEqual(str(self.category), 'admin')

    def test_auto_generate_slug(self):
        self.assertTrue(self.category.slug)
        self.assertEqual(self.category.slug, 'it-one')

    def test_fields_model(self):
        self.assertTrue(self.category.created_at)
        self.assertTrue(self.category.updated_at)
        self.assertIsNotNone(self.category.user)
        self.assertEqual(self.category.color, '#9842f5')
        self.assertTrue(self.category.status)
