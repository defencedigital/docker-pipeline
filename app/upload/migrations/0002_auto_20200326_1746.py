# Generated by Django 3.0 on 2020-03-26 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
