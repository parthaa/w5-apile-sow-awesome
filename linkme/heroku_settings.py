from linkworld.settings import *
import django_heroku

DEBUG = False


django.heroku.settings(locals)
