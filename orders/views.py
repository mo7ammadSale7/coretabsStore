from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail

from accounts.models import Profile
from carts.models import Cart
from .models import Order
from .forms import OrderForm
from .utils import send_email


@login_required
def add_to_order(request):
    cart = Cart.objects.get(user=request.user)
    items = cart.items.all()
    profile = Profile.objects.get(user=request.user)
    if items.exists():
        order = Order.objects.create(
            user=request.user, address=profile.address,)
        order.items.set(items)
        total_price = order.total_price()
        orderitems = order.items.all()
        if request.method == 'POST':
            form = OrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                cart.items.clear()
                send_email(order.user)
                return render(request, 'orders/order-successful.html')
        else:
            form = OrderForm(instance=order)
    else:
        return redirect('products_list')

    context = {
        "form": form,
        "orderitems": orderitems,
        "total_price": total_price,
    }
    return render(request, 'orders/order-add.html', context)
