from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
        return str(self.user)
