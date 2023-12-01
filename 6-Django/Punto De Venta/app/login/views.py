from datetime import date
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView, login_required
from django.views.generic import TemplateView
from cashiers.models import CatalogoCaja
from product.models import Producto
from django.db.models import F
from sales.models import Venta

def root(request):
    return redirect('dashboard')

class dashboard(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Inicio' 
        context["subtitle"] = f'Bienvenido {self.user}'
        today = date.today()
        
        if self.user.rol == 'vendedor':
            ventasHoy = Venta.objects.filter(fecha__year=today.year, fecha__month=today.month, fecha__day=today.day, movimiento_caja__vendedor_encargado=self.user)
            cajas_abiertas = self.user.get_movimiento_caja().caja if self.user.get_movimiento_caja() != None else False
        else:
            ventasHoy = Venta.objects.filter(fecha__year=today.year, fecha__month=today.month, fecha__day=today.day)
            cajas_abiertas = CatalogoCaja.objects.filter(estado_global__exact='abierto').count()
            
        context['ventas_hoy'] = len(ventasHoy)
        context['ganancias_hoy'] = sum (venta.total for venta in ventasHoy)
        context['productos_agotados'] = Producto.objects.filter(existencia__lte=F('existencia_minima')).count()
        context['cajas_abiertas'] = cajas_abiertas
        return context
    
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super().dispatch(request, *args, **kwargs)
    

class LoginFormView(LoginView):
    template_name = "login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Iniciar sesión" 
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)