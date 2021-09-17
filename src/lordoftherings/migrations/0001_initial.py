# Generated by Django 3.2.7 on 2021-09-15 14:17

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('height', models.CharField(max_length=20, null=True)),
                ('race', models.CharField(max_length=255, null=True)),
                ('gender', models.CharField(max_length=255, null=True)),
                ('birth', models.CharField(max_length=255, null=True)),
                ('spouse', models.CharField(max_length=255, null=True)),
                ('death', models.CharField(max_length=255, null=True)),
                ('realm', models.CharField(max_length=255, null=True)),
                ('hair', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('wikiUrl', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('character', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None)),
                ('quote', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('dialog', models.CharField(max_length=255)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lordoftherings.character')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lordoftherings.movie')),
            ],
        ),
    ]
