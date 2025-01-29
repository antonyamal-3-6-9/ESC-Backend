from django.db import models

# Create your models here.

class Transaction(models.Model):
    product = models.ForeignKey('esc_product.Product', on_delete=models.CASCADE, related_name='transactions')
    buyer = models.ForeignKey("esc_trader.Trader", on_delete=models.CASCADE, related_name='purchases')
    transaction_hash = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.buyer.user.username}"
