from django.test import TestCase
from Restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item_str = f'{item.title}: {str(item.price)}'
        self.assertEqual(item_str, "IceCream: 80")