# Generated by Django 3.1.7 on 2021-03-30 07:14

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('item_code', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_list_id', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity_list', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=20, null=True)),
                ('isvisible', models.IntegerField(blank=True, choices=[(1, 'Yes'), (0, 'No')], db_column='ISVISIBLE', default=1, null=True)),
            ],
            options={
                'verbose_name_plural': 'Food',
                'db_table': 'Food',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('ingredient_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('thresholdvalue', models.DecimalField(blank=True, decimal_places=5, default=2.0, max_digits=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'inventory',
                'db_table': 'inventory',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('email', models.CharField(max_length=40, primary_key=True, serialize=False, validators=[django.core.validators.EmailValidator()])),
                ('type', models.CharField(blank=True, choices=[('Owner', 'Owner'), ('Manager', 'Manager'), ('Clerk', 'Clerk')], max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('Otp', models.CharField(blank=True, default='', max_length=7, null=True)),
            ],
            options={
                'verbose_name_plural': 'login',
                'db_table': 'login',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('balance', models.FloatField(db_column='BALANCE', primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Variable',
                'db_table': 'Variable',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('quantity', models.IntegerField(blank=True, db_column='QUANTITY', null=True)),
                ('date', models.DateTimeField(db_column='DATE', default=datetime.datetime(2021, 3, 30, 12, 44, 43, 750682), primary_key=True, serialize=False)),
                ('item_code', models.ForeignKey(blank=True, db_column='ITEM_CODE', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Restaurant.food')),
            ],
            options={
                'verbose_name_plural': 'sales',
                'db_table': 'sales',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('quantity', models.IntegerField(blank=True, db_column='QUANTITY', null=True)),
                ('price', models.FloatField(blank=True, db_column='PRICE', null=True)),
                ('date', models.DateTimeField(db_column='DATE', default=datetime.datetime(2021, 3, 30, 12, 44, 43, 750682), primary_key=True, serialize=False)),
                ('ingredient', models.ForeignKey(db_column='INGREDIENT_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Restaurant.inventory')),
            ],
            options={
                'verbose_name_plural': 'purchase',
                'db_table': 'purchase',
                'managed': True,
            },
        ),
        migrations.AddConstraint(
            model_name='inventory',
            constraint=models.CheckConstraint(check=models.Q(quantity_gte=0), name='quantity_chk_1'),
        ),
        migrations.AddConstraint(
            model_name='food',
            constraint=models.CheckConstraint(check=models.Q(price_gte=0), name='price_chk_1'),
        ),
        migrations.AddConstraint(
            model_name='sales',
            constraint=models.CheckConstraint(check=models.Q(quantity_gte=0), name='quantity_chk_3'),
        ),
        migrations.AddConstraint(
            model_name='purchase',
            constraint=models.CheckConstraint(check=models.Q(price_gte=0), name='price_chk_2'),
        ),
        migrations.AddConstraint(
            model_name='purchase',
            constraint=models.CheckConstraint(check=models.Q(quantity_gte=0), name='quantity_chk_2'),
        ),
    ]
