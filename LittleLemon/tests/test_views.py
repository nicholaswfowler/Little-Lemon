from django.test import TestCase
from Restaurant.models import Menu
from django.core import serializers
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Cheese Pizza", price=12, inventory=50)
        Menu.objects.create(title="Pepperoni Pizza", price=12, inventory=50)
        Menu.objects.create(title="Veggie Pizza", price=12, inventory=50)

    def test_getall(self):
        data = serializers.serialize('json',Menu.objects.all())
        self.assertEqual(data, data)