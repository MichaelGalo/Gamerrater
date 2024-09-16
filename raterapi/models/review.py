from django.db import models
from django.contrib.auth.models import User
from .game import Game


class Review(models.Model):
    content = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content} - {self.game.title} - {self.user.username}"
