from django.contrib.auth import authenticate

from .models import User, Skill
from .serializer import RegisterSerializer, UserSerializer, SkillSerializer

from rest_framework.response import Response
from rest_framework import views, viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class Register(views.APIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        user = self.serializer_class(data=request.data)

        if user.is_valid():
            user.save()
            return Response({
                'message': 'Successfully registered user',
                'user': user.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'message': 'There are errors in the form',
            'error': user.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class Login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user_auth = authenticate(username=username, password=password)

        if user_auth:
            login = self.serializer_class(data=request.data)
            if login.is_valid():
                user = UserSerializer(user_auth)
                return Response({
                    'message': 'Login successful',
                    'access': login.validated_data['access'],
                    'refresh': login.validated_data['refresh'],
                    'user': user.data
                }, status=status.HTTP_200_OK)

        return Response({
            'message': 'Login failed, non-existent user'
        }, status=status.HTTP_404_NOT_FOUND)


class Refresh(TokenRefreshView):
    permission_classes = [IsAuthenticated]


class Logout(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = User.objects.filter(id=request.data.get('user', 0))

        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Logout successful'}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
