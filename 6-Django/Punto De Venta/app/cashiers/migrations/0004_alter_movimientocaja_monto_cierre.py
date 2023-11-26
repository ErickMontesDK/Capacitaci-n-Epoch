# Generated by Django 4.2.6 on 2023-11-09 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashiers', '0003_rename_monto_vendido_movimientocaja_entrada_efectivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientocaja',
            name='monto_cierre',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Monto inicial'),
        ),
    ]