from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import OrderSerializer, PizzaSerializer
from .models import Order, Pizza


# Create your views here.
class OrderList(generics.ListCreateAPIView):
    model = Order
    serializer_class = OrderSerializer
