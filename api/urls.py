from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from . import views

urlpatterns = [
    url(r'^$', views.api_root),
    # # registration form for youngling
    # url(r'^youngling.html/$', views.youngling, name='youngling'),
    # # before answering
    # url(r'^genering.html/(?P<young_id>[0-9]+)/$', views.before_testing, name='before'),
    # # younglings answering
    # url(r'^answering.html/(?P<personal_test_id>[0-9]+)/$', views.testing, name='testing'),
    # # jedies list
    # url(r'^jedies.html/$', views.jedies, name='jedies'),
    # # candidates list
    # url(r'j_y_choosing.html/(?P<selected_jedi_id>[0-9]+)/$', views.j_y_choosing, name='j_y_choosing'),
]
