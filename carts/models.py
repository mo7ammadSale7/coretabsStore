from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

from products.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        User, related_name='cart', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    update_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        total = self.user.cart.items.aggregate(
            Sum('price'))['price__sum'] or 0.00
        return total

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
