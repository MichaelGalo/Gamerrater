from rest_framework import viewsets
from rest_framework import serializers
from raterapi.models import Rating
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = (
            "id",
            "game",
            "score",
            "user",
            "created_at",
        )


class RatingViewSet(viewsets.ModelViewSet):
    """
    A viewset that automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions for the Game model.
    """

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
