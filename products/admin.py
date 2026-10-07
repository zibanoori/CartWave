from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name','slug']
  prepopulated_fields = {"slug":("name",)}  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active', 'is_featured', 'created_at']
    list_filter = ['is_active', 'is_featured','category']
    search_fields = ['name', 'description']
    prepopulated_fields = {"slug": ("name",)}
    
    
    