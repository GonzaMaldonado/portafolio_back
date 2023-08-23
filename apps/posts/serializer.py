from rest_framework import serializers
from .models import Category, Article, Rating

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Article
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    article = serializers.ReadOnlyField(source='article.title')

    class Meta:
        model = Rating
        fields = '__all__'
        