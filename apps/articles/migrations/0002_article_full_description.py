# Generated by Django 4.2.13 on 2024-07-10 19:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='full_description',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Полное описание'),
        ),
    ]
