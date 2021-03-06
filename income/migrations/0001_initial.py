# Generated by Django 4.0.6 on 2022-07-10 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='Nombre de categoria')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipo',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='income.type', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
            },
        ),
    ]
