from django.db import models
from django.contrib.auth.models import AbstractUser
from cashiers.models import MovimientoCaja
from config.settings import MEDIA_URL, STATIC_URL
# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    rol = models.CharField(max_length=13, choices=(('administrador','Administrador'),('vendedor','Vendedor')), default="vendedor")
    genero = models.CharField(max_length=9, choices=(('m','Masculino'),('f','Femenino'),('o','Otro')), default="m", blank=False, null=False)
    
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return  '{}{}'.format(STATIC_URL, 'img/default_user.png')
    
    def get_movimiento_caja(self):
        movimiento_activos = MovimientoCaja.objects.filter(vendedor_encargado = self, fecha_hora_cierre__isnull=True)
        movimiento_activo = movimiento_activos.order_by('-fecha_hora_apertura').first()
        
        return movimiento_activo
