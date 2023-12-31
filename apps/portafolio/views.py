from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import User, Skill
from .serializer import RegisterSerializer, UserSerializer, SkillSerializer, MyTokenObtainPairSerializer

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        login = MyTokenObtainPairSerializer(data=request.data)
        if login.is_valid():
            return Response({
                'access': login.validated_data.get('access'),
                'refresh': login.validated_data.get('refresh'),
                'message': 'Successfully registered user'
                }, status=status.HTTP_201_CREATED)
        return Response({
                'message': 'Usuario registrado, pero no se pudo obtener tokens'
                }, status=status.HTTP_204_NO_CONTENT)
    return Response({
        'error': serializer.errors,
        'message': 'User not created!'
    }, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = super().get_object()

        if user.id != self.request.user.id:
            return self.permission_denied(self.request, 'User unauthorized')
        return user

    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        """ Al tener Register para la creación de usuarios, no necesito un create """
        pass


@api_view(['POST'])
def change_password(request, id):
    if request.user.id == id:
        user = get_object_or_404(User, id=id)
        password = request.data['password']
        user.set_password(password)
        user.save()
        return Response({"message": "Contraseña cambiada con exito"})
    return Response({"error": "Error al cambiar contraseña"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_skills(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills , many=True)
    return Response(serializer.data)

@api_view(['POST'])
def send_email(request):
    name = request.data.get('name', '')
    email = request.data.get('email', '')
    message = request.data.get('message', '')

    if not name or not email or not message:
        return Response({'error': 'All fields are required'})

    # from_email debe ser el email que se utiliza en sendgrid y to_emails no puede ser el mismo, asi que tuve que mandarlo a mi email personal
    mail = Mail(
        from_email='gnmaldo06@gmail.com',
        to_emails='nahuel.maldonado.gonzalo@gmail.com',
        subject='Nuevo mensaje de tu sitio web',
        html_content=f'<strong>Nombre:</strong> {name}<br><strong>Email:</strong> {email}<br><strong>Mensaje:</strong> {message}'
    )

    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(mail)
        return Response({'success': True, 'status': response.status_code})
    except Exception as e:
        return Response({'error': str(e)})
