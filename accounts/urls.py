from django.urls import path, include
from .views import products, logout, login, registration, user_profile
from accounts import urls_reset


urlpatterns = [
    path(r'logout/', logout, name='logout'),
    path(r'login/', login, name='login'),
    path(r'registration/', registration, name='registration'),
    path(r'profile/', user_profile, name='profile'),
    path(r'password_reset/', include(urls_reset)),
]
