from django.contrib.auth.views import PasswordResetView

from django.urls import path

urlpatterns = [
    path(
        '',
        PasswordResetView.as_view(),
        name='password_reset'
    ),
]
