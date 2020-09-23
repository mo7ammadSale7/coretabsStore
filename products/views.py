from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Product


# Create your views here.
def products_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, 'products-list.html', context)
