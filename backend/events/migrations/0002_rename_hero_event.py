# Generated by Django 4.0.5 on 2022-06-10 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hero',
            new_name='Event',
        ),
    ]
