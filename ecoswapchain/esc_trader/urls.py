from django.urls import path
from .views import TraderRegistrationView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('traders/register/', TraderRegistrationView.as_view(), name='trader-register'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)