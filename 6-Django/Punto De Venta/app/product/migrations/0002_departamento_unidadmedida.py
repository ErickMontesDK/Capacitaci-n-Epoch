# Generated by Django 4.2.6 on 2023-11-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=40, unique=True, verbose_name='departamento')),
            ],
            options={
                'verbose_name': 'departamento',
                'verbose_name_plural': 'departamentos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=20, unique=True, verbose_name='unidad de medida')),
            ],
            options={
                'verbose_name': 'unidad de medida',
                'verbose_name_plural': 'unidades de medida',
                'ordering': ['id'],
            },
        ),
    ]
