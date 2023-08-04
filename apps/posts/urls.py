from django.urls import path, include
from .views import ArticleViewSet, CategoryView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'category', CategoryView, basename='categories')

urlpatterns = [
    path('', ArticleViewSet.as_view()),
    path('', include(router.urls)),
]