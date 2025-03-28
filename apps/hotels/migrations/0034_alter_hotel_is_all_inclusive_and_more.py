# Generated by Django 4.2.13 on 2025-03-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0033_remove_hotel_averrage_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='is_all_inclusive',
            field=models.BooleanField(default=False, verbose_name='Все включено ?'),
        ),
        migrations.AlterField(
            model_name='hotelroom',
            name='is_all_inclusive',
            field=models.BooleanField(default=False, verbose_name='Все включено?'),
        ),
    ]
