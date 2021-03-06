from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(
        'change_password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html',
             email_template_name='registration/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]