from django.urls import path, include
from .views import search_products


urlpatterns = [
    path(r'', search_products, name='search')
]