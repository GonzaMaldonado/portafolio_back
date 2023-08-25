from django.db import models
from apps.portafolio.models import User
from django_ckeditor_5.fields import CKEditor5Field

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='posts/categories/')
    slug = models.SlugField(unique=True, max_length=40)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(BaseModel):
    title = models.CharField(max_length=55)
    introduction = models.CharField(max_length=255, default='')
    slug = models.SlugField(unique=True, max_length=55)
    image = models.ImageField(upload_to='posts/articles/')
    body = CKEditor5Field('Text', config_name='extends')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    

    def __str__(self):
        return self.title


class Rating(BaseModel):
    value = models.FloatField()
    comment = models.CharField(max_length=255)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
    