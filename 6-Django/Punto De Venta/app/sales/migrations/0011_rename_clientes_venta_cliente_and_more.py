# Generated by Django 4.2.6 on 2023-11-17 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0010_rename_cliente_venta_clientes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='clienteS',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='descuentoS',
            new_name='descuento',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='fechaS',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='metodo_pagoS',
            new_name='metodo_pago',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='subtotalS',
            new_name='subtotal',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='totalS',
            new_name='total',
        ),
    ]
