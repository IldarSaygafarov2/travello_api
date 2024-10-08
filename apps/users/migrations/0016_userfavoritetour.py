# Generated by Django 4.2.13 on 2024-08-19 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_eventbooking_event_type'),
        ('users', '0015_userhotelsearchhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavoriteTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_tour', to='events.event')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_tour', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Избранный тур пользователя',
                'verbose_name_plural': 'Избранные туры пользователя',
            },
        ),
    ]
