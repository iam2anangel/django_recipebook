from django import forms
from recipebook.models import RecipeAuthor

class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio =  forms.CharField(max_length=2000)

class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    time_required = forms.CharField(max_length=100)
    instructions = forms.CharField(max_length=10000)
    description = forms.CharField(max_length=200, widget=forms.Textarea)

class SudoRecipeAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1000)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(max_length=10000)
    author = forms.ModelChoiceField(queryset=RecipeAuthor.objects.all())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class EditRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    # author = forms.ModelChoiceField(queryset=RecipeAuthor.objects.all)
    description = forms.CharField(max_length=1000)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(max_length=10000)



    
    
    
   
