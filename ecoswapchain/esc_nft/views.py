from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from uploadImage import get_uri
from esc_wallet.models import Wallet
from esc_trader.models import Trader

# Create your views here.

class CreateNFTView(generics.CreateAPIView):
    queryset = NFT.objects.all()
    serializer_class = NFTSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    meta_data = {
        "uri" : None,
        "name" : None,
        "symbol" : None,
    }
    
    def post(self, request, *args, **kwargs):
        try:
            #Save image and metadata to IPFS and get the URI
            self.meta_data = get_uri(request.data.get('metadata'))
            address = Trader.objects.get(eco_user=request.user.eco_user).wallet.private_key
            
            #NFT creation request to the Fastify server, which will create the NFT on the Solana blockchain
            #returns the transaction hash and mint address 
            #Save the NFT to the database
            pass
        except Exception as e:
            return Response({
                "message": "Something went wrong on the server. Try again later."
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)