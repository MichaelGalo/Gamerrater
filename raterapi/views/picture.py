import uuid
import base64
from django.core.files.base import ContentFile
from raterapi.models import Picture
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response


class PictureViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Picture.objects.all()
        serializer = PictureSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        game_image = Picture()
        game_image.user = request.auth.user
        game_image.game = request.data["game_id"]
        format, imgstr = request.data["game_image"].split(";base64,")
        ext = format.split("/")[-1]
        data = ContentFile(
            base64.b64decode(imgstr),
            name=f'{request.data["game_id"]}-{uuid.uuid4()}.{ext}',
        )
        game_image.action_pic = data

        game_image.save()

        serializer = PictureSerializer(game_image, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class PictureSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Picture
        fields = ("id", "game", "user", "uploaded_at", "action_pic")
