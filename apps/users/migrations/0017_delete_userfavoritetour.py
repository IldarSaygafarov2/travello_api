# Generated by Django 4.2.13 on 2024-08-20 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_userfavoritetour'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFavoriteTour',
        ),
    ]