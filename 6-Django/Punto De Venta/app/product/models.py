from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False, verbose_name='Marca', unique=True)
    
    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['id']
    
class UnidadMedida(models.Model):
    unidad = models.CharField(max_length=20, blank=False, null=False, unique=True, verbose_name='unidad de medida')
    
    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'
        ordering = ['id']

    def __str__(self):
        return self.unidad

class Departamento(models.Model):
    nombre = models.CharField(max_length=40, blank=False, null=False, unique=True, verbose_name='departamento')
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['id']

    def __str__(self):
        return self.nombre   

class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=True, unique=True, verbose_name="producto")
    marca = models.ForeignKey("Marca", verbose_name='marca', on_delete=models.CASCADE)
    departamento = models.ForeignKey("Departamento", verbose_name='departamento', blank=True, null=True,on_delete=models.SET_NULL)
    descripcion = models.TextField(blank=True, null=True, verbose_name='descripción')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, verbose_name='precio unitario')
    unidades = models.ForeignKey("UnidadMedida", verbose_name='unidad de medida', blank=False, null=True, on_delete=models.SET_NULL)
    existencia = models.IntegerField(blank=True, null=True, verbose_name='existencia')
    existencia_minima = models.IntegerField(blank=True, null=True, verbose_name='existencia minima')

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"            
        ordering = ['id']

    def __str__(self):
        return self.nombre

