# Generated by Django 3.0 on 2020-03-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20200327_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='theme',
            field=models.CharField(blank=True, choices=[('EC', 'External collab.'), ('IC', 'Internal collab.'), ('UG', 'User guidance'), ('MPP', 'Performance'), ('ES', 'Enabling SECRET')], max_length=15),
        ),
    ]
