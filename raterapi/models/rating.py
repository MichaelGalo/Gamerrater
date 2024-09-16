from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Rating(models.Model):
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("game", "user")

    def __str__(self):
        return f"{self.score} - {self.game.title} - {self.user.username}"
