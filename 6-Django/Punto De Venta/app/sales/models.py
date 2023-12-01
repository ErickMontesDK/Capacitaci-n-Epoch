from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

RAZON_SOCIAL_CHOICES = (
    ('Persona Física', 'Persona Física'), 
    ('Persona Moral', 'Persona Moral'), 
    ('Sociedad Anónima', 'Sociedad Anónima'), 
    ('Sociedad de Responsabilidad Limitada', 'Sociedad de Responsabilidad Limitada'), 
    ('Asociación Civil', 'Asociación Civil'), 
    ('Sociedad en Nombre Colectivo', 'Sociedad en Nombre Colectivo'), 
    ('Sociedad en Comandita Simple', 'Sociedad en Comandita Simple'), 
    ('Sociedad en Comandita por Acciones', 'Sociedad en Comandita por Acciones'), 
    ('Sociedad Cooperativa', 'Sociedad Cooperativa'), 
    ('Sociedad de Capital Variable', 'Sociedad de Capital Variable') 
)

METODO_DE_PAGO = (
    ('efectivo','Efectivo'),
    ('transferencia', 'Transferencia')
)

class Cliente(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, blank=False, null=False, verbose_name="Apellido")
    telefono = PhoneNumberField(null=True, blank=True, unique=True, verbose_name="Teléfono")
    email = models.EmailField(null=False, blank=False,default="dk.erickmontes.coding@gmail.com", verbose_name="Email")
    rfc = models.CharField(max_length=13, null=True, blank=True, verbose_name="R.F.C.")
    razon_social = models.CharField(max_length=36, null=True, blank=True, choices=RAZON_SOCIAL_CHOICES, verbose_name="Razón social")
    direccion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Dirección")
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
        
    def __str__(self):
        return self.nombre +" "+ self.apellido
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
class Venta(models.Model):
    cliente = models.ForeignKey("Cliente", verbose_name='clientes', on_delete=models.DO_NOTHING, default=Cliente.objects.first().pk)
    movimiento_caja = models.ForeignKey("cashiers.MovimientoCaja", verbose_name='movimiento de cajas', null=True,on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="fecha de ventas")
    metodo_pago = models.CharField(max_length=13, blank=False, null=False, choices=METODO_DE_PAGO, verbose_name="método de pagos")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="subtotal de ventas")
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="descuento de ventas")
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="total de venta")
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="monto recibido")
    vuelto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="vuelto dado")
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']
        
    def __str__(self):
        return "{} {} {}".format(self.cliente, self.fecha, self.total)
    
    
class DetalleVenta(models.Model):
    venta = models.ForeignKey("Venta", verbose_name='venta', on_delete=models.CASCADE)
    producto = models.ForeignKey("product.Producto", verbose_name='producto', on_delete=models.DO_NOTHING)
    cantidad_prod = models.IntegerField(blank=True, null=True, verbose_name='existencia')
    importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="importe")
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="descuento")
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="total")
    
    class Meta:
        verbose_name = "Detalle de venta"
        verbose_name_plural = "Detalles de ventas"

    def __str__(self):
        return "Venta: {}. Producto: {}. Cantidad: {}.".format(self.venta, self.producto, self.cantidad_prod)


    
    