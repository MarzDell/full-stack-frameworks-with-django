from django.urls import path, include
from .views import products


urlpatterns = [
    path(r'', products, name='products')
]