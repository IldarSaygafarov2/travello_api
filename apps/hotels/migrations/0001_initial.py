# Generated by Django 4.2.13 on 2024-08-05 19:31

import apps.hotels.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название отеля')),
                ('preview', models.ImageField(upload_to='images/hotels/previews/', verbose_name='Превью фото')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('address', models.CharField(max_length=500, verbose_name='Адрес')),
                ('short_description', models.TextField(verbose_name='Краткое описание')),
                ('full_description', models.TextField(verbose_name='Полное описание')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5, verbose_name='Рейтинг отеля')),
                ('distance_to_beach', models.IntegerField(verbose_name='Расстояние до пляжа, м')),
                ('distance_to_airport', models.IntegerField(verbose_name='Расстояние до аэропорта, км')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('has_wifi', models.BooleanField(default=True, verbose_name='Есть вай-фай?')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
        ),
        migrations.CreateModel(
            name='HotelGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=apps.hotels.models.gallery_image_path, verbose_name='Фото')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_gallery', to='hotels.hotel', verbose_name='Отель')),
            ],
            options={
                'verbose_name': 'Фото отеля',
                'verbose_name_plural': 'Фотки отеля',
            },
        ),
        migrations.CreateModel(
            name='HotelFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Удобство')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facilities', to='hotels.hotel', verbose_name='Отель')),
            ],
            options={
                'verbose_name': 'Удобство отеля',
                'verbose_name_plural': 'Удобства отеля',
            },
        ),
        migrations.CreateModel(
            name='HotelEntertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Развлечение')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entertainment', to='hotels.hotel', verbose_name='Отель')),
            ],
            options={
                'verbose_name': 'Развлечение',
                'verbose_name_plural': 'Развлечения',
            },
        ),
    ]
