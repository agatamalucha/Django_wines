from django.test import TestCase
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.test import Client
from wines.models import WineModel,ColourModel
from django.contrib.auth import get_user_model

WINES_URL = reverse("wines:my-wines")
SEARCH_WINES_URL = reverse("wines:search-wine")


def sample_superuser():
    user = get_user_model().objects.create_superuser(
        username="superuser",
        email="superuser@gmail.com",
        password="test1234",
    )
    return user


class WinesViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.superuser = sample_superuser()
        self.colour = ColourModel.objects.create(
            colour="Test",
        )
        self.wine = WineModel.objects.create(
            name="Test",
            strain="testing",
            image="test",
            price=10.00,
            colour=self.colour,
        )
        self.wine_2 = WineModel.objects.create(
            name="Test1",
            strain="testing",
            image="test1",
            price=11.00,
            colour=self.colour,
        )

    def test_retrieve_my_wines_page(self):
        self.client.login(email='superuser@gmail.com', password='test1234')
        response = self.client.get(WINES_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "my-wines.html")

    def test_retrieve_search_wines(self):
        self.client.login(email='superuser@gmail.com', password='test1234')
        response = self.client.get(SEARCH_WINES_URL, {"query": "testing"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "my-wines.html")
        # print(str(response.context))
        self.assertEqual(len(response.context['queryset']), 2)
        self.assertEqual(len(response.context['wine_types']), 1)




