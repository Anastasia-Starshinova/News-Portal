from django.contrib import admin
from .models import AbstractUser, Author, Category, Post, PostCategory, Comment


admin.site.register(AbstractUser)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
