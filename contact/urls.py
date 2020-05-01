from django.urls import path, include
from django.contrib import admin
from .views import contactview


urlpatterns = [
    path(r'', contactview, name='contact'),
]