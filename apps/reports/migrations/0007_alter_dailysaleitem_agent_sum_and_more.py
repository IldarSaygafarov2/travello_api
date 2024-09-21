# Generated by Django 4.2.13 on 2024-09-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_dailysaleitem_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailysaleitem',
            name='agent_sum',
            field=models.FloatField(default=0, verbose_name='Сумма агент'),
        ),
        migrations.AlterField(
            model_name='dailysaleitem',
            name='comment',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='dailysaleitem',
            name='margin',
            field=models.FloatField(default=0, verbose_name='Маржа'),
        ),
        migrations.AlterField(
            model_name='dailysaleitem',
            name='supplier_sum',
            field=models.FloatField(default=0, verbose_name='Сумма поставщик'),
        ),
    ]