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
    user = request.user
    items = user.cart.items.all()
    if items.exists():
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                mform = form.save(commit=False)
                mform.user = user
                mform.save()
            mform.items.set(items)
            total_price = mform.total_price()
            orderitems = mform.items.all()
            user.cart.items.clear()
            send_email(user)
            context = {
                'total_price': total_price,
                'orderitems': orderitems,
            }
            return render(request, 'orders/order-successful.html', context)
        else:
            form = OrderForm()
    else:
        return redirect('products_list')

    context = {
        "form": form,
    }
    return render(request, 'orders/order-add.html', context)
