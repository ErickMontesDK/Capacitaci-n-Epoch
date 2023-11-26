from django.forms import ModelForm, TextInput
from cashiers.models import CatalogoCaja


class CatalogoCajaForm(ModelForm):
    
    class Meta:
        model = CatalogoCaja
        fields = ("nombre",)
        labels = {
            'nombre': "Nombre de caja"
        }
        widgets = {
            'nombre': TextInput(
                attrs = {
                    'placeholder': "Escriba el nombre de la nueva caja"
                }
            )
        }
