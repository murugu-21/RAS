# Generated by Django 3.1.7 on 2021-04-07 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0014_auto_20210405_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyConsumption',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_id', models.IntegerField(null=True)),
                ('quantity', models.FloatField(null=True)),
                ('date', models.DateField(default=datetime.date(2021, 4, 7))),
            ],
            options={
                'verbose_name_plural': 'DailyConsumption',
                'db_table': 'DailyConsumption',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PurchaseList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=50)),
                ('amount', models.FloatField(null=True)),
                ('is_ordered', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'PurchaseList',
                'db_table': 'PurchaseList',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(db_column='DATE', default=datetime.datetime(2021, 4, 7, 21, 46, 0, 425767), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(db_column='DATE', default=datetime.datetime(2021, 4, 7, 21, 46, 0, 426766), primary_key=True, serialize=False),
        ),
    ]
