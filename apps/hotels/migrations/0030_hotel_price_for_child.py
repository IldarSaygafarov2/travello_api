# Generated by Django 4.2.13 on 2025-02-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0029_hotel_is_all_inclusive'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='price_for_child',
            field=models.IntegerField(blank=True, default=0, help_text='данное поле является не обязательным для заполнения', null=True, verbose_name='цена за ребенка'),
        ),
    ]
