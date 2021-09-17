# Generated by Django 3.2.7 on 2021-09-15 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lordoftherings', '0003_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='favorite',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
    ]