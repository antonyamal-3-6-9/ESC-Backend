from django.db import models
from django.utils.translation import gettext_lazy as _

class NFT(models.Model):
    address = models.CharField(max_length=200, unique=True, db_index=True)  # NFT Mint Address
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=20)  # Usually short, like "NFT"
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="nft_images/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    exchange = models.BooleanField(default=False)

    owner = models.ForeignKey(
        "esc_trader.Trader",
        on_delete=models.CASCADE,
        related_name="owned_nfts"
    )

    product = models.OneToOneField(
        "esc_product.Product",
        on_delete=models.CASCADE,
        related_name="associated_nfts"
    )
    
    leaf_index = models.IntegerField(null=True, blank=True)  # Index of the leaf node
    tree_address = models.CharField(max_length=200, null=True, blank=True)  # Address of the Merkle Tree

    uri = models.URLField(max_length=500)  # IPFS or Arweave metadata link
    timestamp = models.DateTimeField(auto_now_add=True)  # Use DateTime instead of CharField


    status = models.BooleanField(default=False)
    creation = models.OneToOneField("esc_transaction.NFTMintTransaction", verbose_name=_("NFT Mint Transactino"), on_delete=models.CASCADE, related_name="nft_creation")
    
    

    def __str__(self):
        return f"{self.name} ({self.symbol}) - {self.address[:8]}..."
