from rest_framework import viewsets
from rest_framework import serializers
from raterapi.models import Review


class ReviewsSerializer(serializers.ModelSerializer):
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
