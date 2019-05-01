
from django.shortcuts import render
from recipebook.models import Recipe
from recipebook.models import RecipeAuthor

def index(request):
    recipes = Recipe.objects.all()
    html = 'index.html'
    return render(request, html, {'recipes':recipes})

def recipe(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id)
    html = 'recipe.html'
    return render(request, html, {'recipe':recipe})

def author(request, author_id):
    author = RecipeAuthor.objects.filter(user_backend=author_id)
    recipes = Recipe.objects.filter(author_id=author_id)
    html = 'author.html'
    return render(request, html, {'author':author, 'recipes':recipes})