# Generated by Django 4.2.6 on 2023-11-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='negocio',
            name='direccion',
            field=models.CharField(default='ss', max_length=100, verbose_name='Direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='negocio',
            name='nombre',
            field=models.CharField(default='ss', max_length=50, verbose_name='Negocio'),
            preserve_default=False,
        ),
    ]