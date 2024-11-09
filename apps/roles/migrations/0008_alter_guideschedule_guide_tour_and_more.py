# Generated by Django 4.2.13 on 2024-11-04 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0007_guide_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guideschedule',
            name='guide_tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='roles.guidetour', verbose_name='Маршрут тура'),
        ),
        migrations.AlterField(
            model_name='guidetourexpectation',
            name='guide_tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expectations', to='roles.guidetour', verbose_name='Маршрут'),
        ),
        migrations.AlterField(
            model_name='guidetourorganizationaldetail',
            name='guide_tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizational_details', to='roles.guidetour', verbose_name='Маршрут гида'),
        ),
        migrations.AlterField(
            model_name='guidetourphoto',
            name='guide_tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='roles.guidetour', verbose_name='Маршрут тура'),
        ),
        migrations.CreateModel(
            name='GuidePassport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seria_and_number', models.CharField(max_length=100, unique=True, verbose_name='Серия и номер')),
                ('issued_date', models.DateField(verbose_name='Дата выдачи')),
                ('issued_by', models.CharField(max_length=100, verbose_name='Кем выдан')),
                ('citizen', models.CharField(max_length=100, verbose_name='Гражданство')),
                ('agree_to_save_data', models.BooleanField(verbose_name='Согласен на сохранение паспортных данных')),
                ('ready_for_trip', models.BooleanField(verbose_name='Готов к международным поездкам')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passports', to='roles.guide', verbose_name='Гид')),
            ],
            options={
                'verbose_name': 'Паспорт гида',
                'verbose_name_plural': 'Паспортные данные гида',
            },
        ),
    ]