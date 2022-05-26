# Generated by Django 3.2.12 on 2022-05-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='like_users',
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre_ids',
            field=models.ManyToManyField(related_name='genres', to='movies.Genre'),
        ),
    ]