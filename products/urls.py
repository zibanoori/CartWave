from django.urls import path
from .views import index, shop

urlpatterns = [
    path("", index, name="index"),
    path("shop/", shop, name="shop"),
]