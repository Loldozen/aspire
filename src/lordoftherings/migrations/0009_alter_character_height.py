# Generated by Django 3.2.7 on 2021-09-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lordoftherings', '0008_alter_quote_dialog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='height',
            field=models.CharField(max_length=100, null=True),
        ),
    ]