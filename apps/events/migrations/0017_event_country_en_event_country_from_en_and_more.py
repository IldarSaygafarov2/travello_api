# Generated by Django 4.2.13 on 2024-08-10 04:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_eventbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='country_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Страна ивента'),
        ),
        migrations.AddField(
            model_name='event',
            name='country_from_en',
            field=models.CharField(default='Ташкент', max_length=100, null=True, verbose_name='Страна вылета'),
        ),
        migrations.AddField(
            model_name='event',
            name='country_from_ru',
            field=models.CharField(default='Ташкент', max_length=100, null=True, verbose_name='Страна вылета'),
        ),
        migrations.AddField(
            model_name='event',
            name='country_from_uz',
            field=models.CharField(default='Ташкент', max_length=100, null=True, verbose_name='Страна вылета'),
        ),
        migrations.AddField(
            model_name='event',
            name='country_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Страна ивента'),
        ),
        migrations.AddField(
            model_name='event',
            name='country_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Страна ивента'),
        ),
        migrations.AddField(
            model_name='event',
            name='full_description_en',
            field=models.TextField(null=True, verbose_name='Полное описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='full_description_ru',
            field=models.TextField(null=True, verbose_name='Полное описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='full_description_uz',
            field=models.TextField(null=True, verbose_name='Полное описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='gathering_place_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Место сбора группы'),
        ),
        migrations.AddField(
            model_name='event',
            name='gathering_place_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Место сбора группы'),
        ),
        migrations.AddField(
            model_name='event',
            name='gathering_place_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Место сбора группы'),
        ),
        migrations.AddField(
            model_name='event',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='short_description_ru',
            field=models.TextField(null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='short_description_uz',
            field=models.TextField(null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название ивента (Тура)'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название ивента (Тура)'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Название ивента (Тура)'),
        ),
        migrations.AddField(
            model_name='eventpriceincluded',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='eventpriceincluded',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='eventpriceincluded',
            name='title_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='eventpricenotincluded',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='eventpricenotincluded',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='eventpricenotincluded',
            name='title_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='eventtourprogram',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='eventtourprogram',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='eventtourprogram',
            name='description_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='eventtourprogram',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='eventtourprogram',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='eventtourprogram',
            name='title_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
    ]
