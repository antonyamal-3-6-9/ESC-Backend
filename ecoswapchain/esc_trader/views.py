from rest_framework import generics, status
from rest_framework.response import Response
from .models import Trader
from .serializer import TraderRegistrationSerializer, TraderRetrieveSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

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
        response = Response({"access_token": access_token, 'trader' : trader_data}, status=status.HTTP_200_OK)

        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=False,  # HTTPS only
            samesite="Lax"
        )
        return response

class TraderLoginView(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            if Trader.objects.filter(eco_user__email=email).exists():
                trader = Trader.objects.get(eco_user__email=email)
                if trader.eco_user.check_password(password):
                    refresh = RefreshToken.for_user(trader.eco_user)
                    access_token = str(refresh.access_token)
                    trader_data = TraderRetrieveSerializer(trader).data

                    response = Response({"access_token": access_token}, status=status.HTTP_200_OK)

                    response.set_cookie(
                        key="refresh_token",
                        value=str(refresh),
                        httponly=True,
                        secure=False,  # HTTPS only
                        samesite="Lax"
                    )
                    return response
                else: 
                    return Response({
                        "message": "Invalid credentials"
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    "message": "Trader does not exist"
                }, status=status.HTTP_404_NOT_FOUND)
        except KeyError as e:
            return Response({
                "message": "Missing key"
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message": "An error occurred"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    


