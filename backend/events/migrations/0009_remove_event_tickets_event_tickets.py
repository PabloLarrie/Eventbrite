# Generated by Django 4.0.5 on 2022-06-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_location_alter_event_tickets_alter_event_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tickets',
        ),
        migrations.AddField(
            model_name='event',
            name='tickets',
            field=models.ManyToManyField(null=True, related_name='event_tickets', to='events.ticket'),
        ),
    ]
