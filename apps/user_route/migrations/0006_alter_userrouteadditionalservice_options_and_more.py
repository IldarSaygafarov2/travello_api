# Generated by Django 4.2.13 on 2025-04-10 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_route', '0005_userrouteguide_date_from_userrouteguide_date_to_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userrouteadditionalservice',
            options={'verbose_name': 'Дополнительный сервис', 'verbose_name_plural': 'Дополнительные сервисы'},
        ),
        migrations.AlterModelOptions(
            name='userrouteguide',
            options={'verbose_name': 'Гид', 'verbose_name_plural': 'Гиды'},
        ),
        migrations.AlterModelOptions(
            name='usertourhotel',
            options={'verbose_name': 'Отель', 'verbose_name_plural': 'Отели'},
        ),
        migrations.AlterModelOptions(
            name='usertourtransport',
            options={'verbose_name': 'Транспорт', 'verbose_name_plural': 'Транспорты'},
        ),
    ]
