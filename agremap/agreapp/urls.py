from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cities/$', views.cities, name='cities'),
    url(r'^services/$', views.services, name='services'),
    url(r'^chains/$', views.chains, name='chains'),
    url(r'^(?P<city_name>city=[a-z]+)/add/$', views.add, name='add'),
    url(r'^(?P<city_name>city=[a-z]+)/search/$', views.search, name='search'),
    url(r'^(?P<city_name>city=[a-z]+)/searchresult/$', views.searchresult, name='searchresult'),
    url(r'^(?P<city_name>city=[a-z]+)/(?P<organization_id>[0-9]+)/$', views.detailview, name='detailview'),
]