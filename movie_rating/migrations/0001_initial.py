# Generated by Django 3.1 on 2021-02-11 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('popularity', models.FloatField(max_length=10)),
                ('director', models.CharField(max_length=25)),
                ('genre', models.TextField()),
                ('imdb_score', models.FloatField(max_length=3)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
    ]
