from django.db import models
from django.contrib.auth.models import User
from .rating import Rating


class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    age_recommendation = models.IntegerField()
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def average_rating(self):
        ratings = Rating.objects.filter(game=self)
        total = 0
        for rating in ratings:
            total += rating.rating
        if len(ratings) > 0:
            return total / len(ratings)
        else:
            return 0
