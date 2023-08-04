from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import MaxValueValidator
from datetime import date

class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='portafolio/users/', default='portafolio/users/user.png', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True, validators=[MaxValueValidator(date.today())])

    def __str__(self) -> str:
        return self.username


class Skill(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='portafolio/skills/')

    def __str__(self) -> str:
        return self.name