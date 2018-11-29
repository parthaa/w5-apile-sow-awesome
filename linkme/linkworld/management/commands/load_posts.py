from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
from linkworld.models import Post
from mimesis import Person, Text, Internet, Datetime
from random import choice
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    help = "load posts and users dynamically"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        # Post.objects.all().delete()
        # Comment.objects.all().delete()
        users = []
        person = Person()
        for _ in range(10):
            User.objects.create(
                password=person.password(), username=person.username(), first_name=person.name(), last_name=person.last_name(), email=person.email())
        # date = Datetime()

        users = User.objects.all()
        text = Text()
        internet = Internet()
        for _ in range(30):
            title = text.title()
            if not Post.objects.filter(slug=slugify(title)).exists():
                Post.objects.create(author=choice(
                    users), text=text.text(), title=title, url=internet.home_page())
