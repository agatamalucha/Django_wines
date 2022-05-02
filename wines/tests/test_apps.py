from django.test import TestCase

from wines.apps import WinesConfig


class WinesConfigAppTests(TestCase):

    def test_app_name(self):
        self.assertEqual(WinesConfig.name, "wines")
