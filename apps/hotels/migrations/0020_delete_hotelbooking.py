# Generated by Django 4.2.13 on 2024-11-08 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0019_hotelbooking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HotelBooking',
        ),
    ]