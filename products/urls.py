from django.urls import path
from .views import products_list, product_details


urlpatterns = [
    path('products/', products_list, name="products_list"),
    path('products/<pk>/', product_details, name='product_details'),


]
