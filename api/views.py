from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import OrderSerializer, PizzaSerializer
from .models import Order, Pizza


# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    """The entry endpoint of API"""
    return Response({
        'orders'
    })


class OrderList(generics.ListCreateAPIView):
    """API endpoint that represents a list of Orders."""
    model = Order
    serializer_class = OrderSerializer
