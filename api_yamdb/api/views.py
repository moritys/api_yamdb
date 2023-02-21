from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CommentSerializer, ReviewSerializer
from reviews.models import Comment, Review


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        comments = Comment.objects.filter(id=self.review_id)
        return comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        reviews = Review.objects.filter(id=self.title_id)
        return reviews

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
