from rest_framework import viewsets
from raterapi.models import Game, Category
from rest_framework import serializers


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    A viewset that automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions for the Game model.
    """

    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
