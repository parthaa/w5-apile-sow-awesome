from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
from linkworld.models import Post
from mimesis import Person


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        raise NotImplementedError()
