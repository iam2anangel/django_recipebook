# Generated by Django 2.2.1 on 2019-05-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='favorites',
        ),
        migrations.AddField(
            model_name='recipeauthor',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='recipebook.Recipe'),
        ),
    ]