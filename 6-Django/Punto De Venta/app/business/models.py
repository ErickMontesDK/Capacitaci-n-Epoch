from django.db import models
from sales.models import RAZON_SOCIAL_CHOICES
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Negocio(models.Model):
    nombre= models.CharField(null=False, blank=False, max_length=50, verbose_name="Negocio")
    direccion= models.CharField(null=False, blank=False, max_length=100, verbose_name="Direccion")
    telefono = PhoneNumberField(null=True, blank=True, unique=True, verbose_name="Teléfono")
    email = models.EmailField(null=False, blank=False, verbose_name="Email")
    razon_social = models.CharField(max_length=36, null=True, blank=True, choices=RAZON_SOCIAL_CHOICES, verbose_name="Razón social")

    class Meta:
        verbose_name = "Negocio"
        verbose_name_plural = "Negocios"

    def __str__(self):
        return self.name


