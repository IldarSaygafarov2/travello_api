# Generated by Django 4.2.13 on 2024-08-15 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0010_hotel_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='rating',
            new_name='stars',
        ),
    ]