from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
from linkworld.models import Post
from mimesis import Person, Text, Internet, Datetime
from random import choice
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "load posts and users dynamically"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        users = []
        person = Person()
        for _ in range(10):
            User.objects.create_user
        # date = Datetime()
        text = Text()
        internet = Internet()
        users = User.objects.all()
        for _ in range(30):
            post = Post.objects.create(author=choice(
                users), text=text.text(), title=text.title(), url=internet.home_page(), )
            post.save()
