from django.test import TestCase
from Restaurant.models import Menu, Booking

class MenuTest (TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=10)
        self.assertEqual(item, "IceCream : 80")