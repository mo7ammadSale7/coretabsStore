from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from accounts.models import Profile
from carts.models import Cart
from .models import Order


@login_required
def add_to_order(request):
    cart = Cart.objects.get(user=request.user)
    items = cart.items.all()
    profile = Profile.objects.get(user=request.user)
    if items.exists():
        order = Order.objects.create(
            user=request.user, address=profile.address,)
        order.items.set(items)
    else:
        return redirect('products_list')
    user = order.user
    send_mail(
        'order success',
        'your order is success ' + str(user),
        'from@example.com',
        ['to@example.com'],
    )
    return render(request, 'orders/order-successful.html')
