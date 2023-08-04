from django.urls import path, include
from .views import home_posts, all_categories, category_detail, ArticleDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('', home_posts),
    path('categories/', all_categories),
    path('category/<slug:slug>/', category_detail),
    path('article/<slug:slug>/', ArticleDetail.as_view({'get': 'list'})),

]