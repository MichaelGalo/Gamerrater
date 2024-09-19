from rest_framework import viewsets
from raterapi.models import Game, Category, Review
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response


class GameViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Game.objects.all()
        serializer = GameSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Game.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        game = Game()
        game.title = request.data["title"]
        game.designer = request.data["designer"]
        game.description = request.data["description"]
        game.year_released = request.data["yearReleased"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.estimated_time_to_play = request.data["estimatedTimeToPlay"]
        game.age_recommendation = request.data["ageRecommendation"]
        game.user = request.auth.user
        game.save()

        category_ids = request.data.get("categories", [])
        for category_id in category_ids:
            category = Category.objects.get(pk=category_id)
            game.categories.add(category)

        serializer = GameSerializer(game, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "content", "user", "created_at")


class GameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    reviews = ReviewSerializer(many=True, read_only=True, source="review_set")

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
            "reviews",
        )
