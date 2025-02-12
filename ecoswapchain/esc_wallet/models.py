from django.db import models

# Create your models here.

class Wallet(models.Model):
    public_key = models.CharField(max_length=200, unique=True, db_index=True)
    private_key = models.CharField(max_length=200, unique=True, db_index=True)
    balance = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    transactions = models.ManyToManyField("esc_transaction.TokenTransaction", related_name="wallet_transactions")

    def __str__(self):
        return self.public_key