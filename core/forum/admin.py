from django.contrib import admin
from forum.models import Topic, Board, Post

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)
