# Generated by Django 4.0.6 on 2022-08-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='chapter',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='manga',
            name='read_status',
            field=models.CharField(choices=[('RL', 'Read later'), ('R', 'Reading'), ('F', 'Finished')], default='Read later', max_length=15),
        ),
    ]
