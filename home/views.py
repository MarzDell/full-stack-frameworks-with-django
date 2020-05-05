from django.shortcuts import render


def home(request):
    """A view that displays the home page"""
    return render(request, "home.html")
