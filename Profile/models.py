from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    frequency = models.IntegerField()
    amplitude = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField(unique=False, blank=True, null=True)  # Temporarily non-unique
