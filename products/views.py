from django.shortcuts import render, get_object_or_404
from .models import Product
from main.models import SiteConfig

def index(request):
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:6]
    site_config = SiteConfig.objects.first()
    return render(request, "index.html", {"featured_products": featured_products, "site_config": site_config})

def shop(request):
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    site_config = SiteConfig.objects.first()
    return render(request, "shop.html", {
        "products": products,
        "site_config": site_config
        })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    site_config = SiteConfig.objects.first()
    
    
    return render(request, "product_detail.html", {
        "product": product,
        "site_config": site_config
    })
    