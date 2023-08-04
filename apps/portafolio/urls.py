from django.urls import path, include

from .views import register, Login, UserViewSet, get_skills
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('register/', register),
    path('login/', Login.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
    path('skills/', get_skills),
]