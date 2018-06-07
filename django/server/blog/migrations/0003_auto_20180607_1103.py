# Generated by Django 2.0.5 on 2018-06-07 03:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180607_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 7, 3, 3, 10, 939597, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='power',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 7, 3, 3, 10, 939597, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='resume',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
