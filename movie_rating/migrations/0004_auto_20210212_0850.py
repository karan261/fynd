# Generated by Django 3.1 on 2021-02-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_rating', '0003_auto_20210212_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
