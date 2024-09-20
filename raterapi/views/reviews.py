from rest_framework import viewsets
from rest_framework import serializers
from raterapi.models import Review
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class ReviewsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            "id",
            "game",
            "content",
            "user",
            "created_at",
        )


class ReviewsViewSet(viewsets.ModelViewSet):
    """
    A viewset that automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions for the Game model.
    """

    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
