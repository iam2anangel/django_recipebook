# Generated by Django 2.2.1 on 2019-05-01 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeAuthor',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('user_backend', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('time_required', models.CharField(max_length=50)),
                ('instructions', models.TextField(default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipebook.RecipeAuthor')),
            ],
        ),
    ]
