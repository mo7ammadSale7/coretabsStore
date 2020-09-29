from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
