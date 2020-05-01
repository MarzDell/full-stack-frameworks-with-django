from django.urls import path
from .views import view_cart, add_to_cart, adjust_cart


urlpatterns = [
    path(r'', view_cart, name='view_cart'),
    path(r'add/(<id>\d+)', add_to_cart, name='add_to_cart'),
    path(r'adjust/(<id>\d+)', adjust_cart, name='adjust_cart'),
]