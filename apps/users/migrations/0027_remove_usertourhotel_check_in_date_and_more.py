# Generated by Django 4.2.13 on 2024-11-14 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_usertourhotel_check_in_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertourhotel',
            name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='usertourhotel',
            name='departure_date',
        ),
    ]
