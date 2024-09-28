# Generated by Django 4.2.13 on 2024-09-27 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_user_birth_date_alter_user_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[(None, 'Неизвестно'), ('guide', 'Гид'), ('transport_worker', 'Транспортник')], max_length=100, null=True, verbose_name='Тип пользователя'),
        ),
    ]
