# import json
import pytest
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_201_CREATED
from rest_framework.test import APIClient

from api.models import Order


@pytest.mark.django_db
class TestOrderDetail:
    client = APIClient()

    @pytest.fixture
    def order_data(self):
        return {
            'pizza_id': '2',
            'pizza_size': '30',
            'customer_name': 'Test_cust',
            'customer_adress': 'Test_adress'
        }

    @pytest.yield_fixture(scope='function', autouse=True)
    def clean(self):
        Order.objects.all().delete()
        yield

    def test_get(self):
        response = self.client.get('/orders/')
        if Order.objects.all().exists():
            assert response.status_code == HTTP_200_OK
        else:
            assert response.status_code == HTTP_404_NOT_FOUND

    def test_create(self, order_data):
        response = self.client.post('/orders/', order_data)
        assert response.status_code == HTTP_201_CREATED
