from django.db.models import F
from django.http import JsonResponse
from django.views.generic import ListView
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.http import HttpResponse
import django_excel as excel
from django.db.models import Q


def value_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None
    
def value_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None
    
def existence_filter(value):
    try:
        expression = 'existencia__gte' if value == "True" else 'existencia__lte'
        return expression
    except:
        print("Error en la solicitud")

def getQueryFilterOption(campos):
    FILTER_OPTIONS = {
        'id': {
            'query_filter': 'contains',
            'transformValue': value_to_int
        },
        'nombre': {
            'query_filter': 'icontains'
        },
        'username':{
            'query_filter': 'icontains'
        },
        'last_name':{
            'query_filter': 'icontains'
        },
        'first_name':{
            'query_filter':'icontains'
        },
        'email':{
            'query_filter':'startswith'
        },
        'rol':{
            'query_filter':'startswith'
        },
        'genero':{
            'query_filter':'startswith'
        },
        'apellido':{
            'query_filter':'icontains'
        },
        'telefono':{
            'query_filter':'startswith'
        },
        'rfc':{
            'query_filter':'startswith'
        },
        'razon_social':{
            'query_filter':'exact'
        },
        'direccion':{
            'query_filter':'icontains'
        },
        'estado_global':{
            'query_filter':'exact'
        },
        'monto':{
            'query_filter':'startswith',
            'transformValue': value_to_float
        },
        'unidad':{
            'query_filter':'startswith'
        },
        'marca': {
            'sub_field':'marca__nombre',
            'query_filter': 'icontains'
        },
        'departamento': {
            'sub_field':'departamento__nombre',
            'query_filter': 'icontains'
        },
        'descripcion':{
            'query_filter':'icontains'
        },
        'precio_min':{
            'query_filter':'gte',
            'transformValue': value_to_float
        },
        'precio_max':{
            'query_filter':'lte',
            'transformValue': value_to_float
        },
        'unidades':{
            'query_filter':'lte',
            'transformValue': value_to_int
        },
        'existencia':{
            'query_filter':'lte',
            'transformValue': value_to_int
        },
        'existencia_minima':{
            'exception_expression': existence_filter,
            'exception_value':F('existencia_minima')
        },
        'cliente__nombre':{
            'query_filter':'icontains',
            'additional_fields':['cliente__apellido']
        },
        'movimiento_caja__vendedor_encargado__username':{
            'query_filter':'icontains'
        }
        
    }
    filtros = {}
    condicionalDoble = Q()

    for campo, valor in campos.items():
        FILTER_FIELD = FILTER_OPTIONS.get(campo)
        
        if FILTER_FIELD:
            additional_fields = FILTER_FIELD.get('additional_fields')
            if not additional_fields:
                exception_expression = FILTER_FIELD.get('exception_expression')
                exception_value = FILTER_FIELD.get('exception_value')
                if not exception_expression:
                    transformValue = FILTER_FIELD.get('transformValue')
                    FILTER_VALUE = transformValue(valor) if transformValue else valor
                    campo = FILTER_FIELD.get('sub_field') if FILTER_FIELD.get('sub_field') else campo
                    
                    filtros[campo+"__"+FILTER_FIELD.get('query_filter')] = FILTER_VALUE
                else :
                    expression = exception_expression(valor)
                    print(expression,exception_value)
                    filtros[expression]=exception_value
            else:
                print("campo adicional")
                condicion = Q()
                condicion = condicion.__or__(Q(**{campo + "__icontains": valor}))
                
                for aditional_field in additional_fields:
                    condicion = condicion.__or__(Q(**{aditional_field + "__icontains": valor}))
                    
                condicionalDoble= condicion
                
    return filtros, condicionalDoble
            
            
class BaseListView(ListView):
    model = None
    template_name = None
    hideAddElement = False
    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)  
        context['fields'] = self.common_fields

        context["title"] = self.title
        context['subtitle'] = self.subtitle
        context['total_records'] = self.model.objects.count()
        context['add_element'] = self.add_element_url
        context['model'] = self.model.__name__.lower()
        context['list_url'] = self.list_url
        context['hideAddElement'] = self.hideAddElement
        return context
    
    def dispatch(self, request, *args, **kwargs):
        fields = self.model._meta.get_fields()
        self.common_fields = [{'name': field.name, 'type': field.get_internal_type(), 'choices': field.choices if hasattr(field, 'choices') else None} for field in fields]
        if self.filter_range != []:
            self.common_fields = [field for field in self.common_fields if field['name'] in self.filter_range]
            
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        page = int(self.request.GET.get('page', 1))
        orderBy = self.request.GET.get('orderBy', 'id')
        campos = self.request.GET
                
        filters, condicionalOr = getQueryFilterOption(campos)
        
        query = super().get_queryset().filter(**filters).filter(condicionalOr).order_by(orderBy)
                        
        page_size = 10
        pagination = Paginator(query, page_size, 0, True)
        page = pagination.page(page)
        return page, query.count()
    
    def get(self, request, *args, **kwargs):
        self.object_list, query_size = self.get_queryset()
        # descargar_tabla(request)
        context = self.get_context_data(**kwargs) 
                
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            html = render_to_string(self.template_render, context)
            return JsonResponse({"html": html, "query_size":query_size})
        return super().get(request, *args, **kwargs)

class ContextMixin:
    title = ""
    subtitle = ""
    list_name = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context['subtitle'] = self.subtitle
        context['list_url'] = self.list_url
        context['list'] = self.list_name
        context['entity'] = self.model.__name__.lower()
        return context       
    

    
def export_excel_file(request, data):
    # Creamos un objeto de tipo Sheet a partir de los datos usando la función excel.get_sheet
    sheet = excel.pe.Sheet(data)
    return excel.make_response(sheet, "csv")
