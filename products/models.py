from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title
