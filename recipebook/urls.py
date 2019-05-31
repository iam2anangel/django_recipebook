"""django_recipebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from recipebook.admin import admin
from recipebook.views import index, recipe, author, add_author, add_recipe, login_view, signup_view, logout_view, editrecipe, favorite, myfavorites
from recipebook.models import RecipeAuthor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="homepage"),
    path('recipe/<int:recipe_id>/',recipe),
    path('author/<int:author_id>/', author),
    path('addauthor/', add_author),
    path('addrecipe/', add_recipe),
    path('login/', login_view),
    path('signup/', signup_view),
    path('logout/', logout_view),
    path('editrecipe/<int:id>', editrecipe),
    path('favorite/<int:recipe_id>', favorite, name='favorite'),
    path('myfavorites/', myfavorites, name='favorite')
]
