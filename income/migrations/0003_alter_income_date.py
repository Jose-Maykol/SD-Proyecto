# Generated by Django 4.0.6 on 2022-07-10 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0002_alter_type_options_alter_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(blank=True, verbose_name='Fecha'),
        ),
    ]
