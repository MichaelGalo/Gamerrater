from django.db import models
from django.contrib.auth.models import User
from .game import Game


class Picture(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="pictures")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    action_pic = models.ImageField(
        upload_to="actionimages",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
    )

    def __str__(self):
        return f"{self.url} - {self.game.title} - {self.user.username}"
