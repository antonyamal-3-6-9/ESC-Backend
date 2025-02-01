from django.contrib.auth.models import AbstractUser, Group, Permission
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

    password = models.CharField(max_length=128, default="fuckyou")  # Add password field

    groups = models.ManyToManyField(
        Group,
        related_name="eco_user_groups",  # Change related_name to avoid conflict
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="eco_user_permissions",  # Change related_name to avoid conflict
        blank=True
    )

    USERNAME_FIELD = 'email'  # Set email as the unique identifier
    REQUIRED_FIELDS = []  # No other required fields

    def __str__(self):
        return f"{self.email} ({self.role})"
