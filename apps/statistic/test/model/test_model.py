from django import test
from django.contrib.auth import get_user_model

from apps.shortener.models import Shortener
from apps.statistic.models import Statistic


class StatisticModelTestCase(test.TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            email='admin@gmail.com',
            password='admin123123'
        )

        self.shortener = Shortener.objects.create(
            user=self.user,
            long_url='http://google.com',
            short='MyURL'
        )

        self.statistic = Statistic.objects.create(
            ip='95.216.156.142',
            os='Linux',
            browser='google chrome',
            country='Finland',
            language='EN',
            shortener=self.shortener,
        )

    def test_str_method(self):
        self.assertTrue(self.statistic)
        self.assertEqual(str(self.statistic),'95.216.156.142')

    def test_model_fields(self):
        self.assertTrue('time_click')
        self.assertTrue('shortener')
        self.assertEqual(self.statistic.os,'Linux')
        self.assertNotEqual(self.statistic.browser,'sample')
        self.assertEqual(self.statistic.country,'Finland')
        self.assertEqual(self.statistic.language,'EN')