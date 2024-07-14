# Generated by Django 4.2.13 on 2024-07-06 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_passwordreset'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('surname', models.CharField(max_length=100, verbose_name='Отчество')),
                ('birth_date', models.DateField()),
                ('seria', models.CharField(max_length=100, verbose_name='Серия')),
                ('issued_by', models.CharField(max_length=150, verbose_name='Кем выдан')),
                ('issued_date', models.DateField()),
                ('citizen', models.CharField(max_length=100, verbose_name='Гражданство')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passport_data', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Паспортные данные',
                'verbose_name_plural': 'Паспортные данные',
            },
        ),
    ]