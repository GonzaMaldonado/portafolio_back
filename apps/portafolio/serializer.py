from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.portafolio.models import User, Skill


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password')

        if password != confirm_password:
            return serializers.ValidationError('passwords do not match')
        
        return attrs
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['photo'] = user.photo.url
        token['is_staff'] = user.is_staff

        return token


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields  = ['username', 'email', 'first_name', 'last_name']


class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields  = '__all__'