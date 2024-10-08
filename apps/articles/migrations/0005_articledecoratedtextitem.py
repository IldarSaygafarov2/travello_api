# Generated by Django 4.2.13 on 2024-07-22 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_full_description_articletopparagraphs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleDecoratedTextItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decorated_text_items', to='articles.article')),
            ],
        ),
    ]
