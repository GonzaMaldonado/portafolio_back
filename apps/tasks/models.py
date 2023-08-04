from datetime import date
from django.db import models
from django.core.validators import MinValueValidator
from apps.portafolio.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True, null=True)
    important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    time_limit = models.DateTimeField(blank=True, null=True, validators=[MinValueValidator(date.today())])
    completed = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    