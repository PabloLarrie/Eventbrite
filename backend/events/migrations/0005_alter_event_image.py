# Generated by Django 4.0.5 on 2022-06-13 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_ticket_remove_event_price_event_tickets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]