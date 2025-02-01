from django.urls import path
from .views import TraderRegistrationView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register', TraderRegistrationView.as_view(), name='trader-register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)