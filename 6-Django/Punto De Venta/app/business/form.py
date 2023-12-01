from django.forms import EmailInput, ModelForm, TextInput, Textarea
from business.models import Negocio


class NegocioForm(ModelForm):
    class Meta:
        model = Negocio
        fields = '__all__'
        labels = {
            'nombre':'Nombre del negocio',
            'direccion':'Dirección',
            'telefono':'Teléfono',
            'email':'E-mail',
            'razon_social':'Razón social'
        }
        widgets = {
            'nombre':TextInput(
                attrs = {
                    'placeholder':'Escriba el nombre del negocio'
                }
            ),
            'direccion':Textarea(
                    attrs={
                        'placeholder':'Escriba la dirección completa del negocio',
                        'rows': 3
                    }
            ),
            'telefono':TextInput(
                    attrs={
                        'placeholder':'Escriba su teléfono',
                        'pattern':'^\\+?[1-9]\\d{1,14}$' # Validar que sean 10 dígitos
                    }
            ),
            'email':EmailInput(
                    attrs={
                        'placeholder':"Escriba su email"
                    }
            ),
            
        }
        
        