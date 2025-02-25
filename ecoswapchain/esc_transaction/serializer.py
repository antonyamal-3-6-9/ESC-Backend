from rest_framework import serializers
from .models import TokenTransaction, NFTMintTransaction, NFTTransferTransaction

# ✅ Token Transaction Serializer
class TokenTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenTransaction
        fields = "__all__"

# ✅ NFT Mint Transaction Serializer
class NFTMintTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTMintTransaction
        fields = "__all__"

# ✅ NFT Transfer Transaction Serializer
class NFTTransferTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTTransferTransaction
        fields = "__all__"
