from django.db import models

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey('esc_trader.Trader', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_in_crypto = models.DecimalField(max_digits=10, decimal_places=2)  # Crypto price
    image = models.ImageField(upload_to='product_images/')
    nft_id = models.CharField(max_length=255, unique=True, blank=True, null=True)  # Associated NFT
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


