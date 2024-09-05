# Generated by Django 4.2.13 on 2024-09-05 04:51

import apps.main.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticMediaContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=100, unique=True, verbose_name='Название страницы')),
                ('page_slug', models.SlugField(help_text='Данное поле заполнять вручную не нужно', verbose_name='Слаг страницы')),
            ],
            options={
                'verbose_name': 'Статичный медиа контент',
                'verbose_name_plural': 'Статичный медиа контент',
            },
        ),
        migrations.CreateModel(
            name='StaticMediaContentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=True, null=True, upload_to=apps.main.models.static_media_content_file_path, verbose_name='Медиа контет для страницы')),
                ('static_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_content', to='main.staticmediacontent')),
            ],
        ),
    ]
