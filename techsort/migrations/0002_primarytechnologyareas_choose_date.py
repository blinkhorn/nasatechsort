# Generated by Django 2.0.4 on 2018-07-01 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techsort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='primarytechnologyareas',
            name='choose_date',
            field=models.DateTimeField(default='2001-01-01 00:00', verbose_name='date published'),
        ),
    ]
