# Generated by Django 4.2.13 on 2024-11-14 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0022_remove_hotelfacility_hotel_and_more'),
        ('users', '0027_remove_usertourhotel_check_in_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertourhotel',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotels.hotelroom'),
        ),
    ]
