from django.urls import path
from .views import index, shop, product_detail

urlpatterns = [
    path("", index, name="index"),
    path("shop/", shop, name="shop"),
]