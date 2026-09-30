from django.shortcuts import render
from .models import Product

def index(request):
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:6]
    return render(request, "index.html", {"featured_products": featured_products})

def shop(request):
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    return render(request, "shop.html", {"products": products})