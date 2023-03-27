from django import test
from django.contrib.auth import get_user_model
from apps.shortener.models import Category, Shortener
from django.contrib.sites.models import Site


class ShortenerModelTestCase(test.TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='admin@gmail.com',
            password='admin123123'
        )

        self.cat = Category.objects.create(
            title='one',
            color='#9842f5',
            user=self.user
        )

        self.shortener_one = Shortener.objects.create(
            user=self.user,
            category=self.cat,
            long_url='http://google.com',
            short='MyURL'
        )

        self.shortener_two = Shortener.objects.create(
            user=self.user,
            category=self.cat,
            long_url='http://google.com',
            password='password',
        )

    def test_str_method(self):
        self.assertTrue(self.shortener_one)
        self.assertEqual(str(self.shortener_one), 'MyURL')
        self.assertNotEqual(str(self.shortener_one), 'admin')
        self.assertTrue(self.shortener_two)

    def test_auto_generate_short_url(self):
        self.assertTrue(self.shortener_two)
        self.assertIsNotNone(self.shortener_one)

    def test_get_short_url(self):
        self.assertTrue(self.shortener_one.get_short_url)
        self.assertIsNotNone(self.shortener_two.get_short_url)
        self.assertEqual(self.shortener_one.get_short_url, f"https://{Site.objects.get_current().domain}/MyURL")

    def test_set_password(self):
        self.assertTrue(self.shortener_two.set_password)
        self.assertFalse(self.shortener_one.set_password)
