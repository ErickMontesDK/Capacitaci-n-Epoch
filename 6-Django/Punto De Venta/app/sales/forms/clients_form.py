from django.forms import EmailInput, ModelForm, TextInput, Textarea
from sales.models import Cliente


class ClienteForm(ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {
            'nombre': 'Nombre de cliente',
            'apellido': 'Apellidos',
            'telefono': 'Teléfono',
            'Email': 'Correo electrónico',
            'rfc':'R.F.C.',
            'razon_social':'Razón Social',
            'direccion':"Dirección"
        }
        widgets = {
            'nombre':TextInput(
                attrs={
                    'placeholder':'Escriba su nombre',
                }
            ),
            'apellido':TextInput(
                attrs={
                    'placeholder':'Escriba sus apellidos',
                }
            ),
            'teléfono':TextInput(
                attrs={
                    'placeholder':'Escriba su teléfono',
                }
            ),
            'email':EmailInput(
                attrs={
                    'placeholder':"Escriba su email"
                }
            ),
            'rfc':TextInput(
                attrs={
                    'placeholder':'Escriba su R.F.C.',
                }
            ),
            'direccion':Textarea(
                attrs={
                    'placeholder':'Seleccione la razón social',
                    'rows': 3
                }
            ),
        }
        
