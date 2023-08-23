from django.shortcuts import get_object_or_404

from .models import Article, Category, Rating
from .serializer import ArticleSerializer, CategorySerializer, RatingSerializer

from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def home_posts(request):
    """Obtener todos los articulos y categorias"""
    articles = Article.objects.filter(status=True)
    categories = Category.objects.filter(featured=True)
    serializer_articles = ArticleSerializer(articles, many=True)
    serializer_categories = CategorySerializer(categories, many=True)
    return Response({"articles": serializer_articles.data, "navbar_category": serializer_categories.data})

@api_view(['GET'])
def all_categories(request):
    """Obtener todas las categorias de la base de datos."""
    categories = Category.objects.all().order_by('name')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_detail(request, slug):
    """Obtener todos los articulos relacionados a una categoria."""
    category = Category.objects.get(slug=slug)
    articles = Article.objects.filter(categories=category.id)
    serializer_article = ArticleSerializer(articles, many=True)
    serializer_category = CategorySerializer(category, many=False)
    return Response({'articles': serializer_article.data, 'navbar_category': serializer_category.data})

@api_view(['GET'])
def article_detail(request, slug):
    """Obtener detalle de un articulo con todos sus comentarios"""
    article = get_object_or_404(Article,
                                slug=slug,
                                status=True)
    ratings = Rating.objects.filter(article=article.id)
    serializer_article = ArticleSerializer(article, many=False)
    serializer_rating = RatingSerializer(ratings, many=True)
    return Response({'article': serializer_article.data, 'comment': serializer_rating.data})
    

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self):
        
        comment = super().get_object()

        if comment.user.id != self.request.user.id:
            return self.permission_denied(self.request, 'User unauthorized')

        return comment


    
    def create(self, request, *args, **kwargs):
        
        data = request.data.copy()
        article = get_object_or_404(Article, id=data['article'])
        data['article'] = article.id
        data['user'] = request.user.id
        print(data)
        
        rating = self.serializer_class(data=data)
        if rating.is_valid():
            rating.save()
            return Response(rating.data, status=status.HTTP_201_CREATED)
        
        return Response({'error': rating.errors}, status=status.HTTP_400_BAD_REQUEST)