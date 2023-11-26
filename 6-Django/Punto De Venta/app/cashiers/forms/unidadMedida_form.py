from django.forms import ModelForm, TextInput
from product.models import UnidadMedida


class UnidadMedidaForm(ModelForm):
    
    class Meta:
        model = UnidadMedida
        fields = '__all__'
        labels = {
            'unidad':'Unidad de medida'
        }
        widgets = {
            'unidad':TextInput(
                attrs={
                    'placeholder':'Escriba la unidad de medida'
                }
            )
        }
