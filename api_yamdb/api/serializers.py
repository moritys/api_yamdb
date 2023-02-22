from reviews.models import Categories

from rest_framework import serializers


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'
