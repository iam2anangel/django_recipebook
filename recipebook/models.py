from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class RecipeAuthor(models.Model):
    name = models.CharField(max_length=50)
    user_backend = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        primary_key=True,
        default=''
        )
    bio = models.TextField(default='')
    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(RecipeAuthor, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    time_required = models.CharField(max_length=50)
    instructions = models.TextField(default='')

    def __str__(self):
        return self.title