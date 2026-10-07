from django.db import models

class Category(models.Model):
    name = models. CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="products/",blank=True)
    sku = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name
