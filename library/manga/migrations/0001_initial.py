# Generated by Django 4.0.2 on 2022-02-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('read_status', models.CharField(max_length=10)),
                ('chapter', models.IntegerField()),
            ],
        ),
    ]
