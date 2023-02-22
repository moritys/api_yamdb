from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CategoriesSerializer, CommentSerializer, ReviewSerializer
from reviews.models import Categories, Comment, Review


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        comments = Comment.objects.filter(id=self.review_id)
        return comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        reviews = Review.objects.filter(id=self.title_id)
        return reviews

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    # Добавить пермишены и класс пагинации
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
