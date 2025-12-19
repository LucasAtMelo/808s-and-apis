from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('authentication/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('authentication/verify/', TokenVerifyView.as_view(), name='token-verify'),
]
