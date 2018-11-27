from django.contrib import admin

from .models import Post, Vote, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'link', 'title', 'description')
    list_filter = ('author',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'voter', 'post', 'liked')
    list_filter = ('voter', 'post', 'liked')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'author', 'post')
    list_filter = ('author', 'post')
