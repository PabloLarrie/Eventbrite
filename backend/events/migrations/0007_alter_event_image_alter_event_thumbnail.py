# Generated by Django 4.0.5 on 2022-06-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_options_event_slug_event_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]