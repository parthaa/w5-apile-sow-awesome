from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
  link = models.URLField(null=True, blank=True)
  title = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True,  null= True)

  @staticmethod
  def find_with_comments(num_of_comments = 1):
    return Post.objects.annotate(comment_count = models.Count('comments')).filter(comment_count=num_of_comments)

class Vote(models.Model):
  voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="votes")
  post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="votes")
  liked = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True, null= True)

  class Meta:
    unique_together= (('post', 'voter'),)

class Comment(models.Model):
  description = models.TextField(null=True, blank=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
  post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="comments")
  created = models.DateTimeField(auto_now_add=True,  null= True)
