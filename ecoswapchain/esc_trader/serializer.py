from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Trader
from esc_user.models import EcoUser

class TraderRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=8)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    wallet_address = serializers.CharField(required=True)
    store_name = serializers.CharField(required=True)
    mobile_number = serializers.CharField(required=True)

    class Meta:
        model = Trader
        fields = [
            'username', 'email', 'password', 'first_name', 'last_name',
            'wallet_address', 'store_name', 'mobile_number',
        ]

    def create(self, validated_data):
        # Extract user-related data
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')

        # Create User instance
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Create EcoUser instance
        eco_user = EcoUser.objects.create(
            user=user,
            role='TRADER',
            mobile_number=validated_data.pop('mobile_number'),
            email=email
        )

        # Create Trader instance
        trader = Trader.objects.create(
            eco_user=eco_user,
            wallet_address=validated_data.pop('wallet_address'),
            store_name=validated_data.pop('store_name'),
        )

        return trader
