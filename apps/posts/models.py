from django.db import models
from apps.portafolio.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='posts/categories/')
    slug = models.SlugField(unique=True, max_length=40)
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    title = models.CharField(max_length=55)
    introduction = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=55)
    image = models.ImageField(upload_to='posts/articles/')
    body = CKEditor5Field('Text', config_name='extends')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    value = models.FloatField()
    description = models.CharField(max_length=255)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id.username
    