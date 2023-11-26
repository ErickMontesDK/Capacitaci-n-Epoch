from django.forms import ModelForm, Textarea
from product.models import Producto


class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'
        labels = {
            'nombre' : 'Nombre del producto',
            'marca' : 'Marca',
            'departamento' : 'Departamento',
            'descripcion': 'Descripción del producto',
            'precio_unitario' : 'Precio unitario',
            'unidades' : 'Unidad de medida del producto',
            'existencia' : 'Cantidad en existencia',
            'existencia_minima': 'Cantidad mínima en inventario'
        }
        widgets = {
            'descripcion':Textarea(
                attrs={
                    'rows':2
                }
            ) 
        }
