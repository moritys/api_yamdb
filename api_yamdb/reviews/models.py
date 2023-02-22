from django.db import models
from django.contrib.auth import get_user_model


class Title(models.Model):  # Это модель произведения, тут Маша
    pass


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    score = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='titles'
    )

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:15]


class Categories(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='URL категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
