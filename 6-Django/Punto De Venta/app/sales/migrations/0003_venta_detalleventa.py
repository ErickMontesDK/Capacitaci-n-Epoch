# Generated by Django 4.2.6 on 2023-11-13 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_unidad_departamento_nombre'),
        ('sales', '0002_alter_cliente_direccion_alter_cliente_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True, verbose_name='fecha de venta')),
                ('metodo_pago', models.CharField(choices=[('efectivo', 'Efectivo'), ('transferencia', 'Transferencia')], max_length=13, verbose_name='método de pago')),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='subtotal de venta')),
                ('descuento', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='descuento de venta')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='total de venta')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.cliente', verbose_name='cliente')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_prod', models.IntegerField(blank=True, null=True, verbose_name='existencia')),
                ('importe', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='importe')),
                ('descuento', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='descuento')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='total')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.producto', verbose_name='producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.venta', verbose_name='venta')),
            ],
            options={
                'verbose_name': 'Detalle de venta',
                'verbose_name_plural': 'Detalles de ventas',
            },
        ),
    ]
