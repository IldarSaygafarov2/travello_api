# Generated by Django 4.2.13 on 2024-08-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0009_alter_hotel_latitude_alter_hotel_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Город'),
        ),
    ]