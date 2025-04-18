# Generated by Django 4.2.13 on 2025-04-13 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0041_hotel_map_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='map_code_en',
            field=models.TextField(blank=True, null=True, verbose_name='Код для карты'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='map_code_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Код для карты'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='map_code_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Код для карты'),
        ),
    ]
