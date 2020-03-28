from django.conf import settings
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

    THEME_CHOICES = [
        ('EC', 'External collab.'),
        ('IC', 'Internal collab.'),
        ('UG', 'User guidance'),
        ('MPP', 'Performance'),
        ('ES', 'Enabling SECRET'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    phase = models.CharField(max_length=15, choices=PHASE_CHOICES)
    slug = models.SlugField(unique=True, editable=False)
    theme = models.CharField(max_length=15, choices=THEME_CHOICES, blank=True)
    priority = models.PositiveIntegerField(default=0)
    # owner = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=30, blank=True)
    telephone = models.CharField(max_length=30, blank=True)
