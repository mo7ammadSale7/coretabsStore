from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
from .forms import OrderForm
from .utils import send_email
from orders.utils import send_order_email


@login_required
def add_to_order(request):
    user = request.user
    items = user.cart.items.all()
    if items.exists():
        if request.method == 'POST':
            form = OrderForm(request.POST)
            order = form.save(commit=False)
            order.user = user
            order.save()
            order.items.set(items)
            total_price = order.total_price()
            orderitems = order.items.all()
            user.cart.items.clear()
            send_order_email(user, order)
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
