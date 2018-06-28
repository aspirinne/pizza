from django.test import TestCase
from .models import Pizza, Order
# import pytest
# from rest_framework.test import APIClient
# from rest_framework import status
# from rest_framework import reverse


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


class OrderTest(TestCase):
    """This class defines the test suite for the Order model."""
    def setUp(self):
        """Define the test order and other test variables."""
        self.order_pizza = Pizza.objects.create(name='test_pizza_name')
        self.order_pizza_size = '50'
        self.order_customer_name = 'Somebody Test'
        self.order_customer_adress = 'Some Test adress'
        self.order = Order.objects.create(pizza=self.order_pizza, pizza_size=self.order_pizza_size, customer_name=self.order_customer_name, customer_adress=self.order_customer_adress)

    def test_model_can_create_order(self):
        """Test the order model can create a order."""
        old_count = Order.objects.count()
        self.order.save()
        new_count = Order.objects.count()
        self.assertNotEqual(old_count, new_count)
