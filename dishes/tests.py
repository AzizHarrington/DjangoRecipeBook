"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from time import time
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .models import Dish, Ingredient, get_upload_file_name


class DishTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('bob', 'foo@bar.com', '123')

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

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("<h2>Welcome!</h2>", response.content)

    def test_dish_list_view(self):
        d = self.create_dish()
        url = reverse('list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(d.name, response.content)

    def test_dish_detail_view(self):
        d = self.create_dish()
        url = reverse('detail', args=(d.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(d.comments, response.content)

    def test_dish_new_view(self):
        self.client.login(username='bob', password='123')
        url = reverse('new')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 200)
        self.assertIn('<strong>This field is required.</strong>',
            response.content)

        response = self.client.post(url, {'name': 'cake',
                                          'cuisine': 'dessert',
                                          'flavors': 'sweet',
                                          'prep_time': '30',
                                          'ingredients': 'batter',
                                          'comments': 'delicious'})
        self.assertEqual(response.status_code, 300)