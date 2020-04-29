from django.shortcuts import render
from products.models import Product


def search_products(request):
    products = Product.objects.filter(brand_icontains=request.GET['q'])
    return render(request, "products.html", {'products': products})
