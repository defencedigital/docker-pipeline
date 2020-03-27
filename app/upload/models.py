from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Project(models.Model):
    PHASE_CHOICES = [
        ('B', 'Backlog'),
        ('IP', 'In progress'),
        ('RD', 'Ready to deploy'),
        ('L', 'Live'),
        ('R', 'Retired'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    phase = models.CharField(max_length=15, choices=PHASE_CHOICES)
    slug = models.SlugField(unique=True, editable=False)
    # owner = models.ManyToManyField('Owner')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=30, blank=True)
    telephone = models.CharField(max_length=30, blank=True)
