from django.db import models


# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True,)
    image = models.ImageField(upload_to='products/', null=True)

    def __str__(self):
        return self.title
