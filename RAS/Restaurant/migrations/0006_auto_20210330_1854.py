# Generated by Django 3.1.7 on 2021-03-30 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0005_auto_20210330_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(db_column='DATE', default=datetime.datetime(2021, 3, 30, 18, 54, 39, 225073), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(db_column='DATE', default=datetime.datetime(2021, 3, 30, 18, 54, 39, 226073), primary_key=True, serialize=False),
        ),
    ]
