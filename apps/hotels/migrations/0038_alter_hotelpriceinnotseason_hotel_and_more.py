# Generated by Django 4.2.13 on 2025-03-13 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0037_hotelpriceinseason_hotelpriceinnotseason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelpriceinnotseason',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotelroom', verbose_name='Отель'),
        ),
        migrations.AlterField(
            model_name='hotelpriceinseason',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotelroom', verbose_name='Отель'),
        ),
    ]
