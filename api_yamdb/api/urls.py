from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, ReviewViewSet

router = DefaultRouter()

router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments/',
    CommentViewSet,
    basename='comment'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/',
    ReviewViewSet,
    basename='review'
)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', ..., name='register'),  # тут магия Никиты. Вжух!
    path('v1/auth/token/', ..., name='token')  # и тут тоже
]
