from django.urls import path, include

from .views import Register, Login, Refresh, Logout, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('refresh/', Refresh.as_view(), name='refresh'),
    path('logout/', Logout.as_view(), name='logout'),
    path('', include(router.urls)),
]