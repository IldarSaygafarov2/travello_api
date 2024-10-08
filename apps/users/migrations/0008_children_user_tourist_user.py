# Generated by Django 4.2.13 on 2024-07-25 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_tourist_tour_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='children',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tourist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tourist', to=settings.AUTH_USER_MODEL),
        ),
    ]
