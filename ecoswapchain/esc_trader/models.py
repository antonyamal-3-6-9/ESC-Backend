from django.db import models


class Trader(models.Model):
    eco_user = models.OneToOneField("esc_user.EcoUser", on_delete=models.CASCADE, related_name="eco_trader")
    wallet_address = models.CharField(max_length=100, null=True, blank=True)
    total_sales = models.IntegerField(default=0)
    total_purchases = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"    
    