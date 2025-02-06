# products/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    nft_id = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    class Meta:
        model = Product
        fields = ['id', 'seller', 'name', 'description', 'price_in_crypto', 'image', 'created_at']
