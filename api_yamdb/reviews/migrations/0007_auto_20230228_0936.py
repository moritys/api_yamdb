# Generated by Django 3.2 on 2023-02-28 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_alter_review_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments_review', to='reviews.review'),
        ),
    ]
