# Generated by Django 4.0.6 on 2022-07-10 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0003_alter_income_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='category',
            new_name='type',
        ),
    ]
