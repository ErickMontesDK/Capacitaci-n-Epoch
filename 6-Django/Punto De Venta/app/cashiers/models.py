from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Max


class CatalogoCaja(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False, unique=True, verbose_name="Nombre de caja")
    estado_global = models.CharField(max_length=7, blank=False, null=False, choices=(('abierto','Abierto'),('cerrado','Cerrado')),default='cerrado', verbose_name="Estado global")
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default=0, verbose_name="Monto de caja")
    
    class Meta:
        verbose_name = "Catalogo de caja"
        verbose_name_plural = "Catalogo cajas"
        ordering = ['id']
        
    def abrir_caja(self):
        if self.estado_global=='cerrado':
            self.estado_global='abierto'
            self.save()
            return True
        return False
    
    def cerrar_caja(self, monto):
        print('cerrar')
        if self.estado_global == 'abierto':
            self.estado_global = 'cerrado'
            self.monto = monto if monto else self.monto
            self.save()
            return True
        return False

    def get_active_movement(self, user):
        movement = MovimientoCaja.objects.filter(caja=self.id, vendedor_encargado=user, fecha_hora_cierre__isnull=True)        
        movement = movement.order_by('-fecha_hora_apertura').first()

        if movement:
            return movement.id
        return None
    
    def __str__(self):
        return self.nombre
    
class MovimientoCaja(models.Model):
    caja = models.ForeignKey("CatalogoCaja", verbose_name='Tipo de caja', blank=False, null=False, on_delete=models.DO_NOTHING)
    monto_apertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0, verbose_name="Monto inicial")
    monto_cierre = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0, verbose_name="Monto inicial")
    entrada_efectivo = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default=0, verbose_name="Monto vendido")
    salida_efectivo = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default=0, verbose_name="Monto vendido")
    fecha_hora_apertura = models.DateTimeField(auto_now_add=True)
    fecha_hora_cierre = models.DateTimeField(blank=True, null=True)
    vendedor_encargado = models.ForeignKey("users.User", blank=False, null=False, verbose_name="Último vendedor", on_delete=models.DO_NOTHING)
    

    class Meta:
        verbose_name = "MovimientoCaja"
        verbose_name_plural = "MovimientoCajas"

    def __str__(self):
        return f"{self.caja} abierta por {self.vendedor_encargado} | Abierto el {self.fecha_hora_apertura.strftime ('%d/%m/%Y %I:%M %p')}"

    def get_cashier(self):
        return self.caja
