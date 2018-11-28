# scripts/dump_post_data.py
from mimesis import Person, Text, Internet, Datetime
from django.contrib.auth.models import User
from random import choice
from posts.models import Post, Comment

def run():
  person = Person()
  text = Text()
  internet = Internet()
  dateTime = Datetime()

  for i in range(100):
    User.objects.create(password="test1234", username=person.username(), first_name=person.name(),
                          last_name=person.last_name(), email=person.email())

  users = User.objects.all()

  for i in range(100):
    Post.objects.create(author= choice(users), link = internet.home_page(), title=text.title(), description=text.text())

  posts = Post.objects.all()

  for i in range(100):
    Comment.objects.create(author= choice(users), post = choice(posts), description=text.text())