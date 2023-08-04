
from .models import User, Skill
from .serializer import RegisterSerializer, UserSerializer, SkillSerializer, MyTokenObtainPairSerializer

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['POST'])
def register(self, request):
    user = RegisterSerializer(data=request.data)

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
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = super().get_object()

        if user.id != self.request.user.id:
            return self.permission_denied('User unauthorized')
        return user

@api_view(['GET'])
def get_skills(request):

    skills = Skill.objects.all()
    serializer = SkillSerializer(skills , many=True)
    return Response(serializer.data)
