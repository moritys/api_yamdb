from reviews.models import Categories

from rest_framework import viewsets
from rest_framework.filters import SearchFilter
# Добавить пагинацию
# from rest_framework.pagination import 

from .serializers import CategoriesSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    # Добавить пермишены и класс пагинации
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
