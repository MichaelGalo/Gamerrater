from django.db import models
from django.contrib.auth.models import User
from .game import Game


class Rating(models.Model):
    score = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.score} - {self.game.title} - {self.user.username}"
