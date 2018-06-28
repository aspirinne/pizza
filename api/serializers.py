from rest_framework import serializers
from .models import Pizza, Order


class PizzaSerializer(serializers.ModelSerializer):
    """Serializer to map the Pizza.Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the Pizza.model fields."""
        model = Pizza
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Serializer to map the Order.Model instance into JSON format"""

    class Meta:
        """Meta class to map serializer's fields with the Order.model fields."""
        model = Order
        fields = '__all__'
