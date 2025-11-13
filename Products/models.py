from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    active_product = models.BooleanField(default=True)
    slug = models.SlugField(unique=False, blank=True, null=True)  # Temporarily non-unique
    image = models.ImageField(upload_to='images')
