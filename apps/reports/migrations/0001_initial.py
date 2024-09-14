# Generated by Django 4.2.13 on 2024-09-12 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Агент')),
            ],
            options={
                'verbose_name': 'Агент',
                'verbose_name_plural': 'Агенты',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='SupplierReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(verbose_name='Порядковый номер')),
                ('date', models.DateField(verbose_name='Дата')),
                ('agent_sum', models.IntegerField(verbose_name='Сумма агент')),
                ('direction', models.TextField(verbose_name='Направление')),
                ('agent_payment', models.IntegerField(verbose_name='Оплата агент')),
                ('balance', models.IntegerField(verbose_name='Баланс')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Отчет поставщик',
                'verbose_name_plural': 'Отчет поставщик',
            },
        ),
        migrations.CreateModel(
            name='DailySales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(verbose_name='Порядковый номер')),
                ('date', models.DateField(verbose_name='Дата')),
                ('agent_sum', models.IntegerField(verbose_name='Сумма агента')),
                ('supplier_sum', models.IntegerField(verbose_name='Сумма поставщика')),
                ('direction', models.TextField(verbose_name='Направление')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('marja', models.IntegerField(verbose_name='Маржа')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_sales', to='reports.agent', verbose_name='Агент')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_sales', to='reports.supplier', verbose_name='Поставщик')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Дневная продажа',
                'verbose_name_plural': 'Дневные продажи',
            },
        ),
        migrations.CreateModel(
            name='AgentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(verbose_name='Порядковый номер')),
                ('date', models.DateField(verbose_name='Дата')),
                ('agent_sum', models.IntegerField(verbose_name='Сумма агент')),
                ('direction', models.TextField(verbose_name='Направление')),
                ('agent_payment', models.IntegerField(verbose_name='Оплата агент')),
                ('balance', models.IntegerField(verbose_name='Баланс')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'отчет агент',
                'verbose_name_plural': 'отчет агент',
            },
        ),
    ]