from rest_framework import serializers
from esc_user.models import EcoUser  
from .models import Trader

class TraderRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=8)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    class Meta:
        model = Trader
        fields = ['email', 'password', 'first_name', 'last_name']


    def create(self, validated_data):
        # Extract user-related data
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')

        # Create user (EcoUser extending AbstractUser)
        eco_user = EcoUser.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=EcoUser.trader
        )

        # Create Trader instance
        trader = Trader.objects.create(
            eco_user=eco_user,
        )

        trader.verified = True
        trader.save()

        return trader
    
    

class TraderRetrieveSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    wallet_address = serializers.CharField(read_only=True)
    total_sales = serializers.IntegerField(read_only=True)
    total_purchases = serializers.IntegerField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = Trader
        fields = ['first_name', 'last_name', 'wallet_address', 'total_sales', 'total_purchases', 'date_joined', 'verified']