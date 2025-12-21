from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
