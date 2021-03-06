# Generated by Django 3.1.7 on 2021-03-27 02:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_auto_20210326_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='price',
        ),
        migrations.AddField(
            model_name='login',
            name='otp',
            field=models.CharField(blank=True, default='', max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='ingredient',
            field=models.ForeignKey(db_column='INGREDIENT_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Restaurant.inventory'),
        ),
        migrations.AddField(
            model_name='sales',
            name='item_code',
            field=models.ForeignKey(blank=True, db_column='ITEM_CODE', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Restaurant.food'),
        ),
        migrations.AlterField(
            model_name='food',
            name='isvisible',
            field=models.IntegerField(blank=True, choices=[(1, 'Yes'), (0, 'No')], db_column='ISVISIBLE', default=1, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='thresholdvalue',
            field=models.DecimalField(blank=True, decimal_places=5, default=2.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.CharField(max_length=40, primary_key=True, serialize=False, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='type',
            field=models.CharField(blank=True, choices=[('Owner', 'Owner'), ('Manager', 'Manager'), ('Clerk', 'Clerk')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(auto_now=True, db_column='DATE', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateTimeField(auto_now=True, db_column='DATE', primary_key=True, serialize=False),
        ),
        migrations.AddConstraint(
            model_name='food',
            constraint=models.CheckConstraint(check=models.Q(price_gte=0), name='price_chk_1'),
        ),
        migrations.AddConstraint(
            model_name='inventory',
            constraint=models.CheckConstraint(check=models.Q(quantity_gte=0), name='quantity_chk_1'),
        ),
        migrations.AddConstraint(
            model_name='purchase',
            constraint=models.CheckConstraint(check=models.Q(price_gte=0), name='price_chk_2'),
        ),
        migrations.AddConstraint(
            model_name='purchase',
            constraint=models.CheckConstraint(check=models.Q(quantity_gte=0), name='quantity_chk_2'),
        ),
        migrations.AddConstraint(
            model_name='sales',
            constraint=models.CheckConstraint(check=models.Q(quantity_gte=0), name='quantity_chk_3'),
        ),
        migrations.AlterModelTable(
            name='food',
            table='Food',
        ),
    ]
