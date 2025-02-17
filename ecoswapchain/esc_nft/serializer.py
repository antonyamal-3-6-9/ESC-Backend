from rest_framework.serializers import ModelSerializer


class NFTSerializer(ModelSerializer):
    class Meta:
        model = NFT
        fields = ['address', 'name', 'symbol', 'token_id', 'owner', 'product', 'uri', 'timestamp', 'status', 'creation', 'image', 'description']
             