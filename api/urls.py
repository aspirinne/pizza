from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


app_name = 'api'


urlpatterns = [
    url(r'^$', api_root),
    url(r'^orders/$', OrderList.as_view(), name='order-list'),
    # url(r'^orders/?P<customer>\d+/$', OrderList.as_view(), )
    url(r'^orders/?P<pk>\d+/$', OrderDetail.as_view(), name='order-detail'),
    url(r'^pizzas/$', PizzaList.as_view(), name='pizza-list'),
    url(r'^pizzas/?P<pk>\d+/$', PizzaDetail.as_view(), name='pizza-detail'),
]


# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
