# Generated by Django 4.2.13 on 2024-11-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0010_alter_guidepassport_agree_to_save_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='experience',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стаж'),
        ),
    ]
