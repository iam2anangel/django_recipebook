from django import forms
from recipebook.models import RecipeAuthor

class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio =  forms.CharField(max_length=2000)

class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=2000)
    time_required = forms.CharField(max_length=100)
    instructions = forms.CharField(max_length=10000)
    author = forms.ModelChoiceField(queryset=RecipeAuthor.objects.all())