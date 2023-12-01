from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from business.form import NegocioForm
from business.models import Negocio
from django.views.generic import CreateView, UpdateView, View
from shared.utils import ContextMixin

# Create your views here.

class NegocioCheckView(View):
    def get(self, request, *args, **kwargs):
        negocio_exists = Negocio.objects.exists()
        
        if negocio_exists:
            negocio = Negocio.objects.first()
            return redirect('editar_negocio', pk=negocio.id)
        else:
            return redirect('registrar_negocio')

class NegocioCreateView(ContextMixin, CreateView):
    model = Negocio
    success_url = reverse_lazy('dashboard')
    form_class = NegocioForm
    template_name = "negocio_create.html"
    title = 'Ingresar nuevo negocio'
    subtitle = 'Escriba los datos del negocio'
    list_name = ''
    list_url = ""
    
class NegocioUpdateView(ContextMixin, UpdateView):
    model = Negocio
    success_url = reverse_lazy('dashboard')
    form_class = NegocioForm
    template_name = "negocio_create.html"
    title = 'Editar negocio'
    subtitle = 'Edite los datos del negocio necesarios'
    list_name = ''
    list_url = ""
