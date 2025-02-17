from rest_framework import serializers
from esc_wallet.models import Wallet

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
