# Generated by Django 4.2.13 on 2024-07-24 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_children_tourist'),
        ('events', '0009_tourbooking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourbooking',
            name='children',
            field=models.ManyToManyField(blank=True, related_name='tour_children', to='users.children'),
        ),
        migrations.AlterField(
            model_name='tourbooking',
            name='tourists',
            field=models.ManyToManyField(blank=True, related_name='tour_tourists', to='users.tourist'),
        ),
    ]
