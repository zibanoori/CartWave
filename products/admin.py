from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active', 'is_featured', 'created_at']
    list_filter = ['is_active', 'is_featured']
    search_fields = ['name', 'description']
    
    
    