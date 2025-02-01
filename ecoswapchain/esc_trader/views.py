from rest_framework import generics, status
from rest_framework.response import Response
from .models import Trader
from .serializer import TraderRegistrationSerializer, TraderRetrieveSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class TraderRegistrationView(generics.CreateAPIView):
    """
    View for registering a trader (creates User, EcoUser, and Trader instances)
    """
    queryset = Trader.objects.all()
    serializer_class = TraderRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # ✅ Save and get the created trader instance
        trader = serializer.save()

        # ✅ Generate JWT token for the newly created user
        refresh = RefreshToken.for_user(trader.eco_user)
        access_token = str(refresh.access_token)

        # ✅ Use a separate serializer for output
        trader_data = TraderRetrieveSerializer(trader).data

        return Response({
            "message": "Trader registered successfully",
            "access_token": access_token,
            "trader": trader_data  # Return the serialized trader data
        }, status=status.HTTP_201_CREATED)



    


