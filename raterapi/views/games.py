from rest_framework import viewsets
from raterapi.models import Game, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class GameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Game
        fields = (
            "id",
            "title",
            "description",
            "designer",
            "year_released",
            "number_of_players",
            "estimated_time_to_play",
            "age_recommendation",
            "average_rating",
            "categories",
        )


class GameViewSet(viewsets.ModelViewSet):
    """
    A viewset that automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions for the Game model.
    """

    queryset = Game.objects.all()
    serializer_class = GameSerializer
