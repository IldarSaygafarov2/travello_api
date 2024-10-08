# Generated by Django 4.2.13 on 2024-09-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_event_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_event_top',
            field=models.BooleanField(default=False, help_text='Выберите этот пункт, если тур является популряным. Тур отобразится на главной странице', verbose_name='Топовый тур?'),
        ),
    ]
