from datetime import datetime, timezone
from django.contrib import messages
from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from cashiers.forms.movimientocaja_form import MovimientoCajaForm
from cashiers.forms.catalogocaja_form import CatalogoCajaForm
from cashiers.models import *
from shared.utils import BaseListView, ContextMixin, getQueryFilterOption
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from pytz import timezone as tz

class CatalogoCajaListView(BaseListView):
    model = CatalogoCaja
    template_name = 'list.html'
    template_render = 'catalogocaja_table.html'
    title = 'Cajas'
    subtitle = 'Lista de cajas registradas'
    filter_range = ['id', 'nombre','estado_global','monto']
    hideFields = ['monto']
    add_element_url = reverse_lazy('cashier_cat_add')
    list_url = reverse_lazy('cashier_cat_list')
    
    
class MovimientoCajaListView(BaseListView):
    model = MovimientoCaja
    template_name = 'list.html'
    template_render = 'movimientocaja_table.html'
    title = 'Movimientos de Caja'
    subtitle = 'Lista de movimientos de cajas'
    filter_range = ['id','monto_apertura','monto_cierre','fecha_hora_apertura','fecha_hora_cierre','caja','vendedor_encargado']
    hideFields = ['monto_apertura', 'monto_cierre']
    add_element_url = reverse_lazy('cashier_cat_add')
    list_url = reverse_lazy('movements_list')
    hideAddElement = True
    hideActionsColum = True

class CatCajaAbrirListView(BaseListView):
    model = CatalogoCaja
    template_name = 'list.html'
    template_render = 'cajasDisponibles_table.html'
    title = 'Administrador de cajas'
    subtitle = 'Lista de cajas disponibles'
    filter_range = ['id', 'nombre']
    add_element_url = reverse_lazy('cashier_cat_add')
    list_url = reverse_lazy('open_cashier')
    hideAddElement = True
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cajas_disponibles"] = CatalogoCaja.objects.filter(estado_global='cerrado')
        openCashiers = CatalogoCaja.objects.filter(estado_global='abierto')
        openCashierByUser = [{'caja':caja,"movimiento":caja.get_active_movement(self.user.id)} for caja in openCashiers if caja.get_active_movement(self.user.id) is not None]
        if openCashierByUser != []:
            context['movimientos_cajas'] = openCashierByUser
        return context
    
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super().dispatch(request, *args, **kwargs)
    
class MovimientoCajaCreateView(ContextMixin, CreateView):
    model = MovimientoCaja
    template_name = "abrir_caja.html"
    form_class = MovimientoCajaForm
    success_url = reverse_lazy('pantalla_venta')
    list_url = reverse_lazy('open_cashier')
    title = 'Abrir caja'
    list_name = 'Administrador de cajas'
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['subtitle'] = "Abrir caja 'ID:{} - {}'".format(self.cashier.id, self.cashier)
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        valor_inicial = self.cashier.monto
        kwargs['initial'] = {'monto_apertura': valor_inicial, 'monto_cierre':0.00}
        return kwargs
    
    def dispatch(self, request, *args, **kwargs):
        self.cashier = get_object_or_404(CatalogoCaja, pk=self.kwargs.get('catalogo_id'))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        abrio_caja = self.cashier.abrir_caja()
        if abrio_caja:
            form.instance.caja_id = self.cashier.id
            form.instance.vendedor_encargado_id = self.request.user.id
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, "La caja ya se encuentra abierta. Verifique que este cerrada y vuelva a intentarlo")
        return self.render_to_response(self.get_context_data(form=form))


class MovimientoCajaUpdateView(UpdateView):
    model = MovimientoCaja
    template_name = "cerrar_caja.html"
    success_url = reverse_lazy('dashboard')
    form_class = MovimientoCajaForm
    
    def dispatch(self, request, *args, **kwargs):
        catalogo_id = self.kwargs.get('catalogo_id')
        movimiento_id = self.kwargs.get('pk')
        
        self.object = get_object_or_404(MovimientoCaja, caja__id=catalogo_id, pk=movimiento_id)
        self.cashier = get_object_or_404(CatalogoCaja, pk=catalogo_id)
        return super().dispatch(request, *args, **kwargs) 
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context["title"] = "Cerrar caja" 
        context['subtitle'] = "Cerrar caja 'ID:{} - {}'".format(self.cashier.id, self.cashier)
        context['list_url'] = reverse_lazy('open_cashier')
        context['list'] = "Administrador de cajas"
        context['cashier'] = self.cashier
        
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        valor_inicial = self.object.monto_apertura
        ingresos = self.object.entrada_efectivo
        perdidas = self.object.salida_efectivo
        valor_final = valor_inicial+ingresos-perdidas
        kwargs['initial'] = {'monto_apertura':valor_inicial,'monto_cierre':valor_final}
        return kwargs       
            
    def form_valid(self, form):
        monto_cierre = self.request.POST['monto_cierre']
        cerro_caja = self.cashier.cerrar_caja(monto_cierre)
        
        if cerro_caja:
            zona_horaria_mexico = tz('America/Mexico_City')
            hora_actual_mexico = datetime.now(zona_horaria_mexico)
            form.instance.fecha_hora_cierre = hora_actual_mexico
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, "La caja ya se encontraba cerrada. Verifique que estuviera abierta y vuelva a intentarlo")
        return self.render_to_response(self.get_context_data(form=form))

class CatalogoCajaCreateView(CreateView):
    model = CatalogoCaja
    template_name = "create_edit_form.html"
    success_url = reverse_lazy('cashier_cat_list')
    form_class = CatalogoCajaForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva caja" 
        context['subtitle'] = "Agregar nuevo registro de caja"
        context['list_url'] = reverse_lazy('cashier_cat_list')
        context['list'] = "Catálogo de cajas"
        return context

class CatalogoCajaDeleteView(ContextMixin, DeleteView):
    model = CatalogoCaja
    template_name = 'delete_record.html'
    success_url = reverse_lazy('cashier_cat_list')
    list_url = reverse_lazy('cashier_cat_list')
    title = 'Borrar caja'
    subtitle = f'Eliminar registro de cajas'
    list_name = 'Cajas'   


class CatalogoCajaUpdateView(UpdateView):
    model = CatalogoCaja
    template_name = "create_edit_form.html"
    form_class = CatalogoCajaForm
    success_url = reverse_lazy('cashier_cat_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar caja" 
        context['subtitle'] = "Editar registro de caja"
        context['list_url'] = reverse_lazy('cashier_cat_list')
        context['list'] = "Cajas"
        return context


