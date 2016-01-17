from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<city_name>[a-z]+)/$', views.city, name='city'),
    url(r'^(?P<city_name>[a-z]+)/add/$', views.add, name='add'),
    url(r'^(?P<city_name>[a-z]+)/search/$', views.search, name='search'),
    url(r'^(?P<city_name>[a-z]+)/searchresult/$', views.searchresult, name='searchresult'),
    url(r'^(?P<city_name>[a-z]+)/(?P<organization_id>[0-9]+)/$', views.detailview, name='detailview'),
]