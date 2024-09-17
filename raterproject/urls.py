from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from raterapi.views import register_user, login_user, GameViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"games", GameViewSet, basename="game")

urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
]
