# Generated by Django 4.2.13 on 2024-09-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_alter_dailysaleitem_agent_sum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailysaleitem',
            name='date',
            field=models.DateField(default='2024-09-22', verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='dailysales',
            name='date',
            field=models.DateField(default='2024-09-22', verbose_name='Дата'),
        ),
    ]