from django.shortcuts import get_object_or_404, render, redirect

from .models import Product
from .forms import AddProductForm


# Create your views here.
def products_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, 'products/products-list.html', context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
    }
    return render(request, 'products/product-details.html', context)


def product_add(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = AddProductForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return render(request, 'products/product-add-successful.html')
        else:
            form = AddProductForm()
        context = {
            "form": form,
        }
        return render(request, 'products/product-add.html', context)
    else:
        return redirect('products_list')


def product_edit(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            form = AddProductForm(
                request.POST, request.FILES, instance=product)

            if form.is_valid():
                form.save()
                return render(request, 'products/product-add-successful.html')
        else:
            form = AddProductForm(instance=product)
        context = {
            "form": form,
        }
        return render(request, 'products/product-add.html', context)
    else:
        return redirect('products_list')


def product_delete(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('products_list')
    else:
        return redirect('products_list')
