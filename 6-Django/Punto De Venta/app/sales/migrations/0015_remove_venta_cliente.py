# Generated by Django 4.2.6 on 2023-11-17 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0014_alter_venta_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cliente',
        ),
    ]
