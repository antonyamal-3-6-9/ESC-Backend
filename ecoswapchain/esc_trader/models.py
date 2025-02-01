from django.db import models

# Create your models here.

class Trader(models.Model):
    eco_user = models.OneToOneField("esc_user.EcoUser", on_delete=models.CASCADE, related_name="eco_trader")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    wallet_address = models.CharField(max_length=100, null=True, blank=True)
    total_sales = models.IntegerField(default=0)
    total_purchases = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)



