from django.db import models
from django.contrib.auth.models import User
from .rating import Rating
from .category import Category


class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    age_recommendation = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(
        "Category", through="GameCategory", related_name="games"
    )

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = self.ratings.all()

        if ratings:
            return sum(rating.score for rating in ratings) / len(ratings)
        return 0
