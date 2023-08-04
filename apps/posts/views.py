from .models import Article, Category, Rating
from .serializer import ArticleSerializer, CategorySerializer, RatingSerializer

from rest_framework import viewsets, views
from rest_framework.response import Response


class ArticleViewSet(views.APIView):
    serializer_class = ArticleSerializer

    def get(self, request):
        articles = Article.objects.filter(status=True)
        categories = Category.objects.filter(featured=True)
        serializer_article = self.serializer_class(articles, many=True)
        serializer_category = CategorySerializer(categories, many=True)

        print(serializer_article, serializer_category)
        return Response({
            'articles': serializer_article.data,
            'navbar_category': serializer_category.data})
        
        return Response({'message': 'Ocurrio un error en la obtención de articulos y categorias'})
    

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def retrieve(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = self.serializer_class(category)
    
        articles = Article.objects.filter(status=True,
                                          categories=Category.objects.filter(slug=self.kwargs['slug']))
        categories = Category.objects.filter(featured=True)
        serializer_article = ArticleSerializer(articles, many=True)
        serializer_categories = self.serializer_class(categories, many=True)
        return Response({
            'category': serializer.data,
            'articles': serializer_article.data
        })
        