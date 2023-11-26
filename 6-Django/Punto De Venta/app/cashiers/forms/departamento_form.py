from django.forms import ModelForm, TextInput
from product.models import Departamento


class DepartamentoForm(ModelForm):
    
    class Meta:
        model = Departamento
        fields = '__all__'
        labels = {
            'nombre':'Nombre de departamento'
        }
        widgets = {
            'nombre':TextInput(
                attrs={
                    'placeholder':'Escriba el nombre del departamento'
                }
            )
        }
