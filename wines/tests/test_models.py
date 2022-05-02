from django.test import TestCase
from wines.models import WineModel, ColourModel


class ColourModelTests(TestCase):

    def setUp(self):
        self.colour = ColourModel.objects.create(
            colour="Test",
        )

    def tearDown(self):
        self.colour.delete()

    def test_string(self):
        self.assertEqual(str(self.colour), "Test")








class WineModelTests(TestCase):


    def setUp(self):
        self.colour = ColourModel.objects.create(
            colour="Test",
        )
        self.wine = WineModel.objects.create(
            name="Test",
            strain="testing",
            image="test",
            price= 10.00,
            colour= self.colour,
        )

    def tearDown(self):
        self.wine.delete()
        self.colour.delete()

    def test_wine_colour(self):
        self.assertEqual(self.wine.colour.colour, "Test")


    def test_string(self):
        self.assertEqual(str(self.wine), "Test")
