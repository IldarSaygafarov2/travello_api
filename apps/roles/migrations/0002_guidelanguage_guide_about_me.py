# Generated by Django 4.2.13 on 2024-11-03 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=50, verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Язык гида',
                'verbose_name_plural': 'Языки гида',
            },
        ),
        migrations.AddField(
            model_name='guide',
            name='about_me',
            field=models.TextField(blank=True, null=True, verbose_name='О гиде'),
        ),
    ]