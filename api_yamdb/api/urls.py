from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoriesViewSet, CommentViewSet, ReviewViewSet,
    UserViewSet, get_jwt_token, register_user, TitleViewSet, GenreViewSet
    )

router_v1 = DefaultRouter()
router_v1.register(r'users', UserViewSet)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments/',
    CommentViewSet,
    basename='api_comment'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/',
    ReviewViewSet,
    basename='api_review'
)
router_v1.register(
    r'^categories', CategoriesViewSet, basename='api_categories'
)
router_v1.register(
    r'^titles', TitleViewSet, basename='api_titles'
)
router_v1.register(
    r'^genres', GenreViewSet, basename='api_genres'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', register_user, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
