#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript posts
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports
    from django.contrib.auth.models import User

    # Processing model: posts.models.Post

    from posts.models import Post

    posts_post_1 = Post()
    posts_post_1.author =  importer.locate_object(User, "id", User, "id", 1, {'id': 1, 'password': 'pbkdf2_sha256$120000$UI9UHGe237ld$dYf7dgpP+crII5NR9Wdb5kFg3x4gVAeiuXNzS9wnElk=', 'last_login': datetime.datetime(2018, 11, 27, 6, 31, 56, 449061, tzinfo=<UTC>), 'is_superuser': True, 'username': 'admin1', 'first_name': '', 'last_name': '', 'email': 'admin1@admin.com', 'is_staff': True, 'is_active': True, 'date_joined': datetime.datetime(2018, 11, 27, 6, 31, 35, 527568, tzinfo=<UTC>)} )
    posts_post_1.link = 'https://stackoverflow.com/questions/3330435/is-there-an-sqlite-equivalent-to-mysqls-describe-table'
    posts_post_1.title = 'Initial Data'
    posts_post_1.description = 'Cool Description'
    posts_post_1 = importer.save_or_locate(posts_post_1)

    posts_post_2 = Post()
    posts_post_2.author =  importer.locate_object(User, "id", User, "id", 1, {'id': 1, 'password': 'pbkdf2_sha256$120000$UI9UHGe237ld$dYf7dgpP+crII5NR9Wdb5kFg3x4gVAeiuXNzS9wnElk=', 'last_login': datetime.datetime(2018, 11, 27, 6, 31, 56, 449061, tzinfo=<UTC>), 'is_superuser': True, 'username': 'admin1', 'first_name': '', 'last_name': '', 'email': 'admin1@admin.com', 'is_staff': True, 'is_active': True, 'date_joined': datetime.datetime(2018, 11, 27, 6, 31, 35, 527568, tzinfo=<UTC>)} )
    posts_post_2.link = 'https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html'
    posts_post_2.title = 'Reset Generator'
    posts_post_2.description = 'https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html'
    posts_post_2 = importer.save_or_locate(posts_post_2)

    # Processing model: posts.models.Vote

    from posts.models import Vote

    posts_vote_1 = Vote()
    posts_vote_1.voter =  importer.locate_object(User, "id", User, "id", 1, {'id': 1, 'password': 'pbkdf2_sha256$120000$UI9UHGe237ld$dYf7dgpP+crII5NR9Wdb5kFg3x4gVAeiuXNzS9wnElk=', 'last_login': datetime.datetime(2018, 11, 27, 6, 31, 56, 449061, tzinfo=<UTC>), 'is_superuser': True, 'username': 'admin1', 'first_name': '', 'last_name': '', 'email': 'admin1@admin.com', 'is_staff': True, 'is_active': True, 'date_joined': datetime.datetime(2018, 11, 27, 6, 31, 35, 527568, tzinfo=<UTC>)} )
    posts_vote_1.post = posts_post_1
    posts_vote_1.liked = True
    posts_vote_1 = importer.save_or_locate(posts_vote_1)

    posts_vote_2 = Vote()
    posts_vote_2.voter =  importer.locate_object(User, "id", User, "id", 2, {'id': 2, 'password': 'pbkdf2_sha256$120000$jinTG7mXja3N$40OqaBS4RLglac4yCOkhOz/u4yfB5nHmrF5q3zxCUDg=', 'last_login': None, 'is_superuser': False, 'username': 'admin2', 'first_name': '', 'last_name': '', 'email': '', 'is_staff': False, 'is_active': True, 'date_joined': datetime.datetime(2018, 11, 27, 6, 35, 12, 746625, tzinfo=<UTC>)} )
    posts_vote_2.post = posts_post_1
    posts_vote_2.liked = True
    posts_vote_2 = importer.save_or_locate(posts_vote_2)

    # Processing model: posts.models.Comment

    from posts.models import Comment

    posts_comment_1 = Comment()
    posts_comment_1.description = 'My Cool Comment on Post 1 yeh.'
    posts_comment_1.author =  importer.locate_object(User, "id", User, "id", 1, {'id': 1, 'password': 'pbkdf2_sha256$120000$UI9UHGe237ld$dYf7dgpP+crII5NR9Wdb5kFg3x4gVAeiuXNzS9wnElk=', 'last_login': datetime.datetime(2018, 11, 27, 6, 31, 56, 449061, tzinfo=<UTC>), 'is_superuser': True, 'username': 'admin1', 'first_name': '', 'last_name': '', 'email': 'admin1@admin.com', 'is_staff': True, 'is_active': True, 'date_joined': datetime.datetime(2018, 11, 27, 6, 31, 35, 527568, tzinfo=<UTC>)} )
    posts_comment_1.post = posts_post_1
    posts_comment_1 = importer.save_or_locate(posts_comment_1)

