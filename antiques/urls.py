"""antiques URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import urls as urls_home
from accounts import urls as urls_accounts
from products import urls as urls_products
from products.views import all_products
from search import urls as urls_search
from contact import urls as urls_contact


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include(urls_home)),
    path(r'products/', all_products, name='products'),
    path(r'accounts/', include(urls_accounts)),
    path(r'products/', include(urls_products)),
    path(r'search/', include(urls_search)),
    path(r'contact/', include(urls_contact)),
]
