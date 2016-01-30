from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Страница всех городов
    url(r'^cities/$', views.cities, name='cities'),
    url(r'^services/$', views.services, name='services'),
    url(r'^chains/$', views.chains, name='chains'),
    url(r'^clinics/add/$', views.clinics_add, name='clinics_add'),
    # Страница организаций для конкретного города
    url(r'^cities/(?P<city_name>[a-z]+)/$', views.city, name='city'),
    url(r'^cities/(?P<city_name>[a-z]+)/add/$', views.add, name='add'),
    url(r'^cities/(?P<city_name>[a-z]+)/search/$', views.search, name='search'),
    url(r'^cities/(?P<city_name>[a-z]+)/search_result/$', views.search_results, name='search_results'),
    url(r'^cities/(?P<city_name>[a-z]+)/(?P<organization_id>[0-9]+)/$', views.detail_view, name='detail_view'),
]