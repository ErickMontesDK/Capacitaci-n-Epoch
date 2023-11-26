# Generated by Django 4.2.6 on 2023-11-17 18:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from sales.models import Cliente


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_remove_venta_cliente_remove_venta_descuento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(default=Cliente.objects.first().pk, on_delete=django.db.models.deletion.DO_NOTHING, to='sales.cliente', verbose_name='clientes'),
        ),
        migrations.AddField(
            model_name='venta',
            name='descuento',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='descuento de ventas'),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='fecha de ventas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='metodo_pago',
            field=models.CharField(choices=[('efectivo', 'Efectivo'), ('transferencia', 'Transferencia')], default='efectivo', max_length=13, verbose_name='método de pagos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='subtotal de ventas'),
        ),
        migrations.AddField(
            model_name='venta',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='total de venta'),
        ),
    ]