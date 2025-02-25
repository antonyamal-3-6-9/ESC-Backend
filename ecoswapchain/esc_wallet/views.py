from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from .serializer import WalletRetrieveSerializer
from rest_framework.exceptions import NotFound
from esc_trader.models import Trader

class WalletRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = WalletRetrieveSerializer
    
    def get(self, request):
        try:
            trader = Trader.objects.get(eco_user=request.user)  # Get trader instance
            wallet = trader.wallet  # Get wallet field or related object
            
            serializer = self.get_serializer(wallet)  
            return Response({"wallet": serializer.data}, status=status.HTTP_200_OK)
        except NotFound as e:
            return Response({"message": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(str(e))
            return Response({"message": "Something went wrong on the server. Try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)