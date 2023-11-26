from django.urls import reverse_lazy
from cashiers.forms.producto_form import ProductoForm
from cashiers.forms.departamento_form import DepartamentoForm
from cashiers.forms.unidadMedida_form import UnidadMedidaForm
from shared.utils import BaseListView, getQueryFilterOption, ContextMixin
from product.forms.marca_forms import MarcaForm
from product.models import Departamento, Marca, Producto, UnidadMedida
from django.views.generic import DeleteView, UpdateView, CreateView

class MarcaListView(BaseListView):
    model = Marca
    template_name = 'list.html'
    template_render = 'marcas_table.html'
    title = 'Marcas'
    subtitle = 'Lista de marcas'
    filter_range = ['id', 'nombre']
    add_element_url = reverse_lazy('marca_add')
    list_url = reverse_lazy('marcas')


class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = "delete_record.html"
    success_url = reverse_lazy('marcas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Borrar marca" 
        context['subtitle'] = f"Eliminar '{self.object}' de registros de marcas"
        context['list_url'] = reverse_lazy('marcas')
        context['list'] = "Marcas"
        context['entity'] = 'marca'
        return context
    

class MarcaCreateView(CreateView):
    model = Marca
    template_name = "create_edit_form.html"
    form_class = MarcaForm
    success_url = reverse_lazy('marcas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva marca" 
        context['subtitle'] = "Agregar nuevo registro de marca"
        context['list_url'] = reverse_lazy('marcas')
        context['list'] = "Marcas"
        return context
    
class MarcaUpdateView(UpdateView):
    model = Marca
    template_name = "create_edit_form.html"
    form_class = MarcaForm
    success_url = reverse_lazy('marcas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar marca" 
        context['subtitle'] = "Editar registro de marca"
        context['list_url'] = reverse_lazy('marcas')
        context['list'] = "Marcas"
        return context
    
class UnidadMedidaListView(BaseListView):
    model = UnidadMedida
    template_name = 'list.html'
    template_render = 'unidades_table.html'
    title = 'Unidades de medida'
    subtitle = 'Lista de unidades de medida'
    filter_range = ['id', 'unidad']
    add_element_url = reverse_lazy('unit_add')
    list_url = reverse_lazy('units_list')
    
class UnidadMedidaCreateView(ContextMixin, CreateView):
    model = UnidadMedida
    template_name = "create_edit_form.html"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('units_list')
    list_url = reverse_lazy('units_list')
    title = 'Nueva unidad'
    subtitle = 'Agregar nuevo registro de unidad'
    list_name = 'units_list'
    
class UnidadMedidaUpdateView(ContextMixin, UpdateView):
    model = UnidadMedida
    template_name = "create_edit_form.html"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('units_list')
    list_url = reverse_lazy('units_list')
    title = 'Editar unidad'
    subtitle = 'Editar registro de unidad'
    list_name = 'Unidades de medida'
    
class UnidadMedidaDeleteView(ContextMixin, DeleteView):
    model = UnidadMedida
    template_name = 'delete_record.html'
    success_url = reverse_lazy('units_list')
    list_url = reverse_lazy('units_list')
    title = 'Borrar unidad'
    subtitle = f'Eliminar registro de unidad de medida'
    list_name = 'Unidades de medida'

class DepartamentoListView(BaseListView):
    model = Departamento
    template_name = 'list.html'
    template_render = 'departamentos_table.html'
    title = 'Departamentos'
    subtitle = 'Lista de departamentos'
    filter_range = ['id', 'nombre']
    add_element_url = reverse_lazy('department_add')
    list_url = reverse_lazy('departments')
    
class DepartamentoCreateView(ContextMixin, CreateView):
    model = Departamento
    template_name = "create_edit_form.html"
    form_class = DepartamentoForm
    success_url = reverse_lazy('departments')
    list_url = reverse_lazy('departments')
    title = 'Nuevo departamento'
    subtitle = 'Agregar nuevo registro de departamento'
    list_name = 'Departamentos'
    
class DepartamentoUpdateView(ContextMixin, UpdateView):
    model = Departamento
    template_name = "create_edit_form.html"
    form_class = DepartamentoForm
    success_url = reverse_lazy('departments')
    list_url = reverse_lazy('departments')
    title = 'Editar departamento'
    subtitle = 'Editar registro de departamento'
    list_name = 'Departamentos'
    
class DepartamentoDeleteView(ContextMixin, DeleteView):
    model = Departamento
    template_name = 'delete_record.html'
    success_url = reverse_lazy('departments')
    list_url = reverse_lazy('departments')
    title = 'Borrar departamento'
    subtitle = f'Eliminar registro de departamentos'
    list_name = 'Departamentos'
    
class ProductoListView(BaseListView):
    model = Producto
    template_name = 'productos_list.html'
    template_render = 'productos_table.html'
    title = 'Productos'
    subtitle = 'Lista de productos'
    filter_range = ['id','nombre', 'marca','departamento','descripcion','precio_unitario','unidades','existencia','existencia_minima']
    add_element_url = reverse_lazy('product_add')
    list_url = reverse_lazy('products_list')
    
class ProductoCreateView(ContextMixin, CreateView):
    model = Producto
    template_name = "producto_form.html"
    form_class = ProductoForm
    success_url = reverse_lazy('products_list')
    list_url = reverse_lazy('products_list')
    title = 'Nuevo producto'
    subtitle = 'Agregar nuevo registro de producto'
    list_name = 'Productos'
    
class ProductoUpdateView(ContextMixin, UpdateView):
    model = Producto
    template_name = "create_edit_form.html"
    form_class = ProductoForm
    success_url = reverse_lazy('products_list')
    list_url = reverse_lazy('products_list')
    title = 'Editar producto'
    subtitle = 'Editar registro de producto'
    list_name = 'Productos'
    
class ProductoDeleteView(ContextMixin, DeleteView):
    model = Producto
    template_name = 'delete_record.html'
    success_url = reverse_lazy('products_list')
    list_url = reverse_lazy('products_list')
    title = 'Borrar producto'
    subtitle = f'Eliminar registro de producto'
    list_name = 'Productos'