from rest_framework import serializers
from esc_wallet.models import Wallet
from esc_transaction.serializer import TokenTransactionSerializer

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['public_key', 'private_key', 'balance']  # 'key' is intentionally excluded

    def create(self, validated_data):
        """Override create method to securely hash and store the encryption key."""
        key = self.context.get('key')  # Retrieve key from context (NOT from validated_data)
        wallet = Wallet.objects.create(**validated_data)  # Save validated data

        if key:
            wallet.set_key(key)  # Hash and store the encryption key securely

        return wallet

class WalletRetrieveSerializer(serializers.ModelSerializer):
    sent_transaction = TokenTransactionSerializer(source="sent_token_transactions", many=True)
    recieved_transaction = TokenTransactionSerializer(source="received_token_transactions", many=True)
    class Meta:
        model = Wallet
        fields = ['public_key', 'balance', 'sent_transaction', 'recieved_transaction']
        