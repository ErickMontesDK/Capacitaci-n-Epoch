# Generated by Django 4.2.6 on 2023-11-17 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0011_rename_clientes_venta_cliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='descuento',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='metodo_pago',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='total',
        ),
    ]