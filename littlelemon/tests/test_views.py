from django.test import TestCase
from Restaurant.models import Menu, Booking
from Restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        Menu.objects.create(name='Pizza', price=10.99, category='Main Course')
        Menu.objects.create(name='Burger', price=8.99, category='Main Course')
        Menu.objects.create(name='Salad', price=6.99, category='Appetizer')

    def test_getall(self):
        # Retrieve all Menu objects using the API endpoint
        client = APIClient()
        url = reverse('menu-list')  # Replace 'menu-list' with the actual name of your API endpoint
        response = client.get(url)

        # Get the expected serialized data of all Menu objects
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the serialized data in the response equals the expected serialized data
        self.assertEqual(response.data, serializer.data)






