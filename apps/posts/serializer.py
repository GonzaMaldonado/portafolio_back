from rest_framework import serializers
from .models import Category, Article, Rating
from apps.portafolio.models import User

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    user_id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    #user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Rating
        fields = '__all__'
        