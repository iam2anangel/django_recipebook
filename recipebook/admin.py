from django.contrib import admin
from .models import RecipeAuthor, Recipe

admin.site.register(RecipeAuthor)
admin.site.register(Recipe)