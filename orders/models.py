from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum

from products.models import Product

User = get_user_model()


class Order(models.Model):
    address = models.CharField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)

    def total_price(self):
        total = self.items.aggregate(
            Sum('price'))['price__sum'] or 0.00
        return total

    def __str__(self):
        return str(self.user)
