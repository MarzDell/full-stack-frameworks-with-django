from django.shortcuts import render
from products.models import Product


def search_products(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {'products': products})
