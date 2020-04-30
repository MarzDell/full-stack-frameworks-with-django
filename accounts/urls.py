from django.conf.urls import url, include
from .views import products, logout, login, registration, user_profile
from accounts import urls_reset


urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^profile/$', user_profile, name='profile'),
    url(r'^password_reset/', include(urls_reset)),
]