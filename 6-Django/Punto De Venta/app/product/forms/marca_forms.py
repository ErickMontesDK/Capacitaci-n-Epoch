from django.forms import ModelForm, TextInput
from product.models import Marca

class MarcaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Marca
        fields = '__all__'
        labels = {
            'nombre': 'Nombre de la marca'
        }
        widgets = {
            'nombre': TextInput(
                attrs = {
                    'placeholder':'Escriba el nombre de la marca'
                }
            ),
        }
