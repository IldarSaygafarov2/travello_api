# Generated by Django 4.2.13 on 2024-11-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_event_is_event_top'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='corporate_client_price',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Цена для корпоративных клиентов'),
        ),
    ]