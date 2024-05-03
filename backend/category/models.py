from django.db import models
from colorfield.fields import ColorField


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    color = ColorField(format="hexa")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
