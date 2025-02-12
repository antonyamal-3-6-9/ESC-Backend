from django.db import models

# Create your models here.
class TokenTransaction(models.Model):
    transaction_hash = models.CharField(max_length=200, unique=True, db_index=True)
    time_stamp = models.DateTimeField(auto_now_add=True, db_index=True)
    amount = models.BigIntegerField()
    
    transfered_to = models.ForeignKey(
        "esc_trader.Trader", 
        verbose_name=_("Receiver"), 
        on_delete=models.CASCADE, 
        related_name="received_token_transactions"
    )
    transfered_from = models.ForeignKey(
        "esc_trader.Trader", 
        verbose_name=_("Sender"), 
        on_delete=models.CASCADE, 
        related_name="sent_token_transactions"
    )

    TRANSACTION_TYPES = [
        ("BUY", "Buy"),
        ("SELL", "Sell"),
        ("REWARD", "Reward"),
    ]
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)

    # ✅ New Fields
    network_fees = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)  # Transaction Fee
    status = models.CharField(max_length=20, choices=[("PENDING", "Pending"), ("CONFIRMED", "Confirmed"), ("FAILED", "Failed")], default="PENDING")
    block_number = models.BigIntegerField(null=True, blank=True)  # Block where the transaction was confirmed

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.transaction_hash[:10]}"

class NFTMintTransaction(models.Model):
    transaction_hash = models.CharField(max_length=200, unique=True, db_index=True)
    time_stamp = models.DateTimeField(auto_now_add=True, db_index=True)

    minted_to = models.ForeignKey(
        "esc_trader.Trader", 
        verbose_name=_("Minted To"), 
        on_delete=models.CASCADE, 
        related_name="minted_nfts"
    )

    # ✅ New Fields
    nft_name = models.CharField(max_length=100)  # Name of the NFT
    nft_symbol = models.CharField(max_length=10, default="NFT")  # Token symbol
    metadata_uri = models.URLField(null=True, blank=True)  # IPFS link to metadata
    mint_cost = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)  # Minting cost
    mint_status = models.CharField(max_length=20, choices=[("PENDING", "Pending"), ("CONFIRMED", "Confirmed"), ("FAILED", "Failed")], default="PENDING")

    def __str__(self):
        return f"NFT {self.nft_name} minted to {self.minted_to} - {self.transaction_hash[:10]}"


class NFTTransferTransaction(models.Model):
    transaction_hash = models.CharField(max_length=200, unique=True, db_index=True)
    time_stamp = models.DateTimeField(auto_now_add=True, db_index=True)

    transfered_to = models.ForeignKey(
        "esc_trader.Trader", 
        verbose_name=_("Receiver"), 
        on_delete=models.CASCADE, 
        related_name="received_nfts"
    )
    transfered_from = models.ForeignKey(
        "esc_trader.Trader", 
        verbose_name=_("Sender"), 
        on_delete=models.CASCADE, 
        related_name="sent_nfts"
    )

    # ✅ New Fields
    nft_name = models.CharField(max_length=100)  # Name of NFT
    nft_id = models.CharField(max_length=200, db_index=True)  # Unique NFT Identifier (Mint Address)
    previous_owner_duration = models.IntegerField(null=True, blank=True)  # Duration the previous owner held the NFT (in days)
    transfer_reason = models.TextField(null=True, blank=True)  # Reason for the transfer (optional)

    def __str__(self):
        return f"Transferred {self.nft_name} from {self.transfered_from} to {self.transfered_to} - {self.transaction_hash[:10]}"
