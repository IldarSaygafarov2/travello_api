# Generated by Django 4.2.13 on 2024-09-16 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailysales',
            name='serial_number',
        ),
    ]