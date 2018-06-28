from django.test import TestCase
from .models import Pizza, Order
# import pytest
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework import reverse


# Create your tests here.

class PizzaTest(TestCase):
    """This class defines the test suite for the Pizza model."""
    def setUp(self):
        """Define the test pizza and other test variables."""
        self.pizza_name = 'test_pizza_name'
        self.pizza = Pizza.objects.create(name=self.pizza_name)

    def test_model_can_create_pizza(self):
        """Test the pizza model can create a pizza."""
        old_count = Pizza.objects.count()
        self.pizza.save()
        new_count = Pizza.objects.count()
        self.assertNotEqual(old_count, new_count)
#
#
# class OrderTest(TestCase):
#     """This class defines the test suite for the Order model."""
#     def setUp(self):
#         """Define the test order and other test variables."""
#         self.order_pizza = Pizza.objects.create(name='test_pizza_name')
#         self.order_pizza_size =
