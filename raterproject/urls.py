from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
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
    PictureViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"games", GameViewSet, basename="game")
router.register(r"categories", CategoriesViewSet, basename="category")
router.register(r"reviews", ReviewsViewSet, basename="review")
router.register(r"users", UserViewSet, basename="users")
router.register(r"rating", RatingViewSet, basename="rating")
router.register(r"upload_image", PictureViewSet, basename="image")

urlpatterns = [
    path("", include(router.urls)),
    path("register", register_user),
    path("login", login_user),
    path("current_user", current_user, name="current_user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
