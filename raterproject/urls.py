from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from raterapi.views import (
    register_user,
    login_user,
    current_user,
    GameViewSet,
    CategoriesViewSet,
    ReviewsViewSet,
    UserViewSet,
    RatingViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"games", GameViewSet, basename="game")
router.register(r"categories", CategoriesViewSet, basename="category")
router.register(r"reviews", ReviewsViewSet, basename="review")
router.register(r"users", UserViewSet, basename="users")
router.register(r"rating", RatingViewSet, basename="rating")

urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("current_user", current_user, name="current_user"),
]
