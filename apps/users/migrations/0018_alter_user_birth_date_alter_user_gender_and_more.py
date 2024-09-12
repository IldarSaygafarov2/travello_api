# Generated by Django 4.2.13 on 2024-09-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_delete_userfavoritetour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
