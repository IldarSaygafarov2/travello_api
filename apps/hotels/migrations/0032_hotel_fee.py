# Generated by Django 4.2.13 on 2025-03-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0031_alter_hotel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='fee',
            field=models.FloatField(default=0.0, verbose_name='Наценка'),
        ),
    ]
