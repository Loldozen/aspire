# Generated by Django 3.2.7 on 2021-09-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lordoftherings', '0007_movie_budgetinmillions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='dialog',
            field=models.TextField(),
        ),
    ]
