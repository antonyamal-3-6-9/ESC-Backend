from django.contrib.auth.models import User
from django.db import models

# User roles
USER_ROLES = [
    ('ADMIN', 'Admin'),
    ('TRADER', 'Trader'),
    ('SHIPPING_HUB_ADMIN', 'Shipping Hub Admin'),
]

class EcoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=USER_ROLES)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
