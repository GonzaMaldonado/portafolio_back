from django.urls import path, include

from .views import register, UserViewSet, get_skills, change_password, send_email
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('register/', register),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
    path('change_password/<int:id>/', change_password),
    path('skills/', get_skills),
    path('send_email/', send_email),
]