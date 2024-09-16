from django.db import models
from django.contrib.auth.models import User
from .game import Game


class Picture(models.Model):
    url = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url} - {self.game.title} - {self.user.username}"
