from django.db import models
from django.utils.translation import gettext_lazy as _

class NFT(models.Model):
    address = models.CharField(max_length=200, unique=True, db_index=True)  # NFT Mint Address
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=20)  # Usually short, like "NFT"
    token_id = models.CharField(max_length=200, unique=True, db_index=True)  # Unique Token Identifier

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

    uri = models.URLField(max_length=500)  # IPFS or Arweave metadata link
    timestamp = models.DateTimeField(auto_now_add=True)  # Use DateTime instead of CharField


    status = models.models.BooleanField(default=False)

    lifecycle = models.ManyToManyField(
        "esc_transaction.NFTTransferTransaction",
        verbose_name=_("NFT Transfer History"),
        related_name="nft_lifecycle",
        blank=True
    )
    
    creation = Models.models.OneToOneField("esc_transactions.NFTMintTransaction", verbose_name=_("NFT Mint Transactino"), on_delete=models.CASCADE, related_name="nft_creation")

    def __str__(self):
        return f"{self.name} ({self.symbol}) - {self.address[:8]}..."
