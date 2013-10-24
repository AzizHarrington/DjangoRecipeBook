"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from time import time
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Dish, get_upload_file_name


class DishTest(TestCase):
    def create_dish(self, name="cake", cuisine="dessert",
                    flavors="sweet", prep_time="30", comments="delicious"):
        return Dish.objects.create(name=name,
                                   cuisine=cuisine,
                                   flavors=flavors,
                                   prep_time=prep_time,
                                   comments=comments)

    def test_dish_creation(self):
        d = self.create_dish()
        self.assertTrue(isinstance(d, Dish))
        self.assertEqual(d.__unicode__(), d.name)

    def test_get_upload_file_name(self):
        filename = "cake.jpg"
        path = "uploaded/%s_%s" % (str(time()).replace('.', '_'), filename)
        created_path = get_upload_file_name(self, filename)
        self.assertEqual(path, created_path)

    def test_dish_list_view(self):
        d = self.create_dish()
        url = reverse('list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(d.name, response.content)
