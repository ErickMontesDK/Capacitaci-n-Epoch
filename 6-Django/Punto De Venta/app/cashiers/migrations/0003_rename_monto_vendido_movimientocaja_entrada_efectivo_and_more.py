# Generated by Django 4.2.6 on 2023-11-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashiers', '0002_rename_catalogocajas_catalogocaja_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movimientocaja',
            old_name='monto_vendido',
            new_name='entrada_efectivo',
        ),
        migrations.RenameField(
            model_name='movimientocaja',
            old_name='fecha_hora_abrio',
            new_name='fecha_hora_apertura',
        ),
        migrations.RenameField(
            model_name='movimientocaja',
            old_name='fecha_hora_cerro',
            new_name='fecha_hora_cierre',
        ),
        migrations.RenameField(
            model_name='movimientocaja',
            old_name='monto_inicial',
            new_name='monto_apertura',
        ),
        migrations.RenameField(
            model_name='movimientocaja',
            old_name='vendedor_abrio',
            new_name='vendedor_encargado',
        ),
        migrations.AddField(
            model_name='movimientocaja',
            name='monto_cierre',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Monto inicial'),
        ),
        migrations.AddField(
            model_name='movimientocaja',
            name='salida_efectivo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Monto vendido'),
        ),
        migrations.AlterField(
            model_name='catalogocaja',
            name='estado_global',
            field=models.CharField(choices=[('abierto', 'Abierto'), ('cerrado', 'Cerrado')], default='cerrado', max_length=7, verbose_name='Estado global'),
        ),
    ]
