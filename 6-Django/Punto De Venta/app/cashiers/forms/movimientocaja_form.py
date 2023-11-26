from django.forms import HiddenInput, ModelForm, NumberInput
from cashiers.models import MovimientoCaja


class MovimientoCajaForm(ModelForm):
    
    class Meta:
        model = MovimientoCaja
        exclude = ['caja', 'vendedor_encargado','fecha_hora_cierre'] 
        fields = ("monto_apertura","monto_cierre")
        labels = {
            'monto_apertura':"Monto inicial",
            'monto_cierre':"Monto final"
        }
        widgets = {
            'monto_apertura':NumberInput(
                attrs={
                    "placeholder":0.00,
                    "step":"Any"
                }
            ),
            'monto_cierre':NumberInput(
                attrs={
                    "placeholder":0.00,
                    "step":"Any"
                }
            ),
            'caja': HiddenInput(), 
            'vendedor_encargado': HiddenInput(),  
        }
