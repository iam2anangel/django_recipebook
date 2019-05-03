
from django.shortcuts import render
from django.contrib.auth.models import User
from recipebook.models import Recipe
from recipebook.models import RecipeAuthor
from recipebook.forms import AuthorAddForm, RecipeAddForm

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

def add_recipe(request):
    html='add_recipe.html'
    form = None
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return render(request,'addrecipesuccess.html')
    else:
        form = RecipeAddForm()
    return render(request, html, {'form': form})

def add_author(request):
    html='add_author.html'
    form = None
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(
                username=data['name'],
            )
            RecipeAuthor.objects.create(
                name=data['name'],
                bio=data['bio'],
                user_backend=user
            )
            return render(request, 'addauthorsuccess.html')
    else:
        form = AuthorAddForm()
    return render(request, html, {'form': form})