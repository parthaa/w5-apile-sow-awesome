# Generated by Django 2.1.3 on 2018-11-27 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_vote_liked'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set(),
        ),
    ]
