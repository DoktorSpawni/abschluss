from .models import Post, User, Follow, Like
from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Like)