# Generated by Django 4.0.6 on 2022-07-11 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0004_rename_category_income_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Fecha'),
        ),
    ]
