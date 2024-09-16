from django.db import models
from django.contrib.auth.models import User
from .game import Game


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
