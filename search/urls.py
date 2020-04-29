from django.conf.urls import url, include
from .views import search_products


urlpatterns = [
    url(r'^$', search_products, name='search')
]