from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
  link = models.TextField(null=True, blank=True)
  title = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)

class Vote(models.Model):
  voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="votes")
  post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="votes")
  liked = models.BooleanField(default=False)

  class Meta:
    unique_together= (('post', 'voter'),)

class Comment(models.Model):
  description = models.TextField(null=True, blank=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
  post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="comments")