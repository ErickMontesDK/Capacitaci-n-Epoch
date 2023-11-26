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
from shared.utils import BaseListView, getQueryFilterOption
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
    add_element_url = reverse_lazy('cashier_cat_add')
    list_url = reverse_lazy('cashier_cat_list')


class MovimientoCajaListView(ListView):
    model = MovimientoCaja
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        fields = self.model._meta.get_fields()
        fieldsToShow = ['id','monto_apertura','monto_cierre','fecha_hora_apertura','fecha_hora_cierre','caja','vendedor_encargado']
        context = super().get_context_data(**kwargs)
        context['fields'] = [{'name':field.name, 'type':field.get_internal_type(), 'choices':field.choices if hasattr(field, 'choices') else None} for field in fields if field.name in fieldsToShow] 
        context["title"] = "Movimientos de caja" 
        context['subtitle'] = "Lista de movimientos de cajas "
        context['total_records'] = MovimientoCaja.objects.count()
        context['model'] = 'movimiento de caja'
        context['list_url'] = reverse_lazy('movements_list')
        context['hideAddElement'] = True
        context['hideActionsColum'] = True
        return context
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        page = int(self.request.GET.get('page', 1))
        orderBy = self.request.GET.get('orderBy', 'id')
        query = super().get_queryset().order_by(orderBy)
        campos = self.request.GET
                
        filters, condicionalOr = getQueryFilterOption(campos)
        
        if filters != {}:
            query = query.filter(**filters)

        page_size = 10
        
        pagination = Paginator(query, page_size, 0, True)
        page = pagination.page(page)
        return page, query.count()
    
    def get(self, request, *args, **kwargs):
        self.object_list, query_size = self.get_queryset() 
        context = self.get_context_data(**kwargs) 
        
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            template_name = "movimientocaja_table.html"
            html = render_to_string(template_name, context)
            return JsonResponse({"html": html, "query_size":query_size})
        return super().get(request, *args, **kwargs)
    
    
class CatCajaAbrirListView(ListView):
    model = CatalogoCaja
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        fields = self.model._meta.get_fields()
        fieldsToShow = ['id', 'nombre']
        context = super().get_context_data(**kwargs)
        context['fields'] = [{'name':field.name, 'type':field.get_internal_type(), 'choices':field.choices if hasattr(field, 'choices') else None} for field in fields if field.name in fieldsToShow] 
        context["title"] = "Administrador de cajas" 
        context['subtitle'] = "Lista de cajas disponibles"
        context['total_records'] = CatalogoCaja.objects.count()
        context['model'] = 'catálogo de caja'
        context['list_url'] = reverse_lazy('open_cashier')
        context['hideAddElement'] = True
        context['cajas_disponibles'] = CatalogoCaja.objects.filter(estado_global='cerrado')
        openCashiers = CatalogoCaja.objects.filter(estado_global='abierto')
        openCashierByUser = [{'caja':caja,"movimiento":caja.get_active_movement(self.user.id)} for caja in openCashiers if caja.get_active_movement(self.user.id) is not None]
        if openCashierByUser != []:
            context['movimientos_cajas'] = openCashierByUser

        return context
    
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        campos = self.request.GET
        page = int(self.request.GET.get('page', 1))
        orderBy = self.request.GET.get('orderBy', 'id')
        query = super().get_queryset().order_by(orderBy)
                        
        filters, condicionalOr = getQueryFilterOption(campos)
        
        if filters != {}:
            query = query.filter(**filters)

        page_size = 10
        
        pagination = Paginator(query, page_size, 0, True)
        page = pagination.page(page)
        return page, query.count()
    
    def get(self, request, *args, **kwargs):
        self.object_list, query_size = self.get_queryset() 
        context = self.get_context_data(**kwargs) 
        
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            template_name = "cajasDisponibles_table.html"
            html = render_to_string(template_name, context)
            return JsonResponse({"html": html, "query_size":query_size})
        return super().get(request, *args, **kwargs)    
    


class MovimientoCajaCreateView(CreateView):
    model = MovimientoCaja
    template_name = "abrir_caja.html"
    success_url = reverse_lazy('dashboard')
    form_class = MovimientoCajaForm
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context["title"] = "Abrir caja" 
        context['subtitle'] = "Abrir caja 'ID:{} - {}'".format(self.cashier.id, self.cashier)
        context['list_url'] = reverse_lazy('open_cashier')
        context['list'] = "Administrador de cajas"
        context['cashier'] = self.cashier
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
        print('pandashow')
        monto_cierre = self.request.POST['monto_cierre']
        cerro_caja = self.cashier.cerrar_caja(monto_cierre)
        
        print(self.cashier.estado_global)
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
    
class CatalogoCajaDeleteView(DeleteView):
    model = CatalogoCaja
    template_name = "delete_record.html"
    success_url = reverse_lazy('cashier_cat_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Borrar caja" 
        context['subtitle'] = f"Eliminar '{self.object}' de registros de cajas"
        context['list_url'] = reverse_lazy('cashier_cat_list')
        context['list'] = "Cajas"
        context['entity'] = 'caja'
        return context
    
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


