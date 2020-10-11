from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required


from products.models import Product
from .models import Cart


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.items.add(product)
    return redirect('cart')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.items.remove(product)
    return redirect('cart')


@login_required
def clear_cart(request):
    cart = Cart.objects.get(user=request.user)
    products = cart.items
    products.clear()
    return redirect('cart')


@login_required
def cart(request):
    user = request.user
    products = user.cart.items.all()
    total_price = user.cart.total_price()
    context = {
        'products': products,
        'total_price': total_price
    }
    return render(request, 'carts/cart.html', context)
