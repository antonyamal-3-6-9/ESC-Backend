from rest_framework import generics, status
from rest_framework.response import Response
from .models import Trader
from .serializer import TraderRegistrationSerializer


class TraderRegistrationView(generics.CreateAPIView):
    """
    View for registering a trader (creates User, EcoUser, and Trader instances)
    """
    queryset = Trader.objects.all()
    serializer_class = TraderRegistrationSerializer

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trader = serializer.save()
        return Response({
            "message": "Trader registered successfully",
            "trader_id": trader.id,
            "eco_user_id": trader.eco_user.id,
            "username": trader.eco_user.user.username,
        }, status=status.HTTP_201_CREATED)
    



    


