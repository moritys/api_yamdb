from django.contrib import admin

from .models import User, Categories, Comment, Review, Title 


admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Title)
admin.site.register(Review)
admin.site.register(Comment)
