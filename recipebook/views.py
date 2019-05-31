from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from recipebook.models import RecipeAuthor, Recipe, User
from recipebook.forms import AuthorAddForm, RecipeAddForm, LoginForm, SignupForm, SudoRecipeAddForm, EditRecipeForm



def index(request):
    recipes = Recipe.objects.all()
    current_user = request.user.username
    greeting = f'Welcome {current_user}' if current_user else 'Not logged in'
    html = 'index.html'
    return render(request, html, {'recipes':recipes, 'greeting': greeting})

def recipe(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    html = 'recipe.html'
    return render(request, html, {'recipe':recipe})

def author(request, author_id):
    author = RecipeAuthor.objects.filter(user_backend=author_id)
    # favorites = author[0].favorites.get_queryset()
    recipes = Recipe.objects.filter(author_id=author_id)
    html = 'author.html'
    return render(request, html, {'author':author, 'recipes':recipes})

@login_required()
def add_recipe(request):
    html='add_recipe.html'
    form = None
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                author = data['author']
            except:
                author = request.user.recipeauthor
            Recipe.objects.create(
                title=data['title'],
                # author=data['author'],
                author=author,
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return render(request, 'addrecipesuccess.html')
    else:
        if request.user.is_staff:
            form = SudoRecipeAddForm
        else:
            form = RecipeAddForm()
    return render(request, html, {'form': form})

@login_required
@staff_member_required
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
    return render(request,html,{'form': form})

def login_view(request):
    html='main_form.html'
    form = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next','/'))
    else:
        form = LoginForm()
    return render(request, html, {'form': form, 'title': 'login'})

def signup_view(request):
    html = 'main_form.html'
    form = None

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['username'], data['password'])
                # data['username'], data['email'], data['password'])
            login(request, user)
            RecipeAuthor.objects.create(
                name=data['username'],
                user_backend=user
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = SignupForm()
    return render(request, html, {'form': form, 'title': 'signup'})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required()
def editrecipe(request, id):
    html = 'edit_recipe.html'
    form = None
    recipe = Recipe.objects.filter(id=id)
    title = Recipe.objects.filter(id=id).values_list('title', flat=True).first()
    author = Recipe.objects.filter(id=id).values_list('author', flat=True).first()
    description = Recipe.objects.filter(id=id).values_list('description', flat=True).first()
    time_required = Recipe.objects.filter(id=id).values_list('time_required', flat=True).first()
    instructions = Recipe.objects.filter(id=id).values_list('instructions', flat=True).first()
    if request.method == 'POST':
        form = EditRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.update(
                title=data['title'],
                # author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions'],
            )
        return render(request, 'updated_recipe.html')
    else:
        form = RecipeAddForm(initial={'title': title, 'author': author, 'description': description, 'time_required': time_required, 'instructions': instructions})
    return render(request, html, {'form': form})


@login_required()
def myfavorites(request):
    html = 'favorites.html'
    page_options = {}
    if request.user.author:
        recipes = request.user.author.favorites.all()
        page_options.update({"recipes": recipes})
    return render(request, html, page_options)


def favorite(request, recipe_id):
    """To favorite a recipe """
    user = request.user.author
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe not in user.favorites.all():
        user.favorites.add(recipe)
    elif recipe in user.favorites.all():
        user.favorites.remove(recipe)
    return HttpResponseRedirect(reverse('recipe', kwargs={"recipe_id": recipe_id}))




