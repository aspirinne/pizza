# from django.shortcuts import render
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
        'orders': reverse('order-list', request=request),
        'pizzas': reverse('pizza-list', request=request),
    })


class OrderList(generics.ListCreateAPIView):
    """API endpoint that represents a list of Orders."""
    model = Order
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        customer = self.request.query_params.get('customer')

        if customer:
            queryset = queryset.filter(customer_name=customer)

        return queryset


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that represent a single order."""
    model = Order
    serializer_class = OrderSerializer


class PizzaList(generics.ListCreateAPIView):
    """API endpoint that represents a list of Pizzas."""
    model = Pizza
    serializer_class = PizzaSerializer


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that represent a single pizza."""
    model = Pizza
    serializer_class = PizzaSerializer
