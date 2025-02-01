from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLES = [
    ('admin', 'Admin'),
    ('trader', 'Trader'),
    ('shipping', 'Shipping'),
]

class EcoUser(AbstractUser):

    admin='Admin'
    trader='Trader'
    shipping='Shipping'

    username = None  # Remove the default username field
    email = models.EmailField(unique=True)  # Use email as the username
    role = models.CharField(max_length=20, choices=USER_ROLES)

    USERNAME_FIELD = 'email'  # Set email as the unique identifier
    REQUIRED_FIELDS = []  # No other required fields

    def __str__(self):
        return f"{self.email} ({self.role})"
