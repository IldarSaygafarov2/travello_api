# Generated by Django 4.2.13 on 2024-07-24 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_tourist_tour_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourist',
            name='tour_booking',
        ),
    ]
